#!/usr/bin/env python3
"""Combines two independent evidence reports. Does NOT assert peer-review certification."""
from __future__ import annotations
import argparse, collections, json, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
COURSE_ROOT = HERE.parent
MANDATORY_DEEP = (
    'feature_frozendict','feature_sentinel','feature_unpack_comprehension','feature_lazy_import',
    'original_C07.02','original_C07.03','original_C07.04','original_F05.02',
    'library_numpy','library_pandas_cow3','library_sklearn','library_torch_cpu','library_pyarrow'
)
OPTIONAL_TRACKS = ('library_tensorflow','gpu_torch_cuda','free_threaded_no_gil','native_abi_compiled_extension')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--full',type=Path,required=True,help='strict full 536-case run_validation.py report')
    p.add_argument('--deep',type=Path,required=True,help='strict run_deep_validation.py report')
    p.add_argument('--keras',type=Path,required=True,help='Keras runtime evidence from CPython 3.15.2')
    p.add_argument('--pip-check',type=Path,required=True,help='Successful pip check output')
    p.add_argument('--output',type=Path,default=HERE/'CERTIFICATION_GATE_RESULT.json')
    a=p.parse_args()
    full=json.loads(a.full.read_text(encoding='utf8'))
    deep=json.loads(a.deep.read_text(encoding='utf8'))
    # Both runners must provide independent runtime/version evidence.
    full_315 = bool(full.get('strict_verified_runtime') and full.get('implementation')=='cpython' and '3.15.2' in full.get('runner',''))
    deep_315 = bool(deep.get('target_runtime_executed') and '3.15.2' in deep.get('interpreter',''))
    rows={v['test']:v for v in deep.get('results',[])}
    missing=[x for x in MANDATORY_DEEP if rows.get(x,{}).get('status')!='PASS_TARGET_3152']
    full_rows=full.get('results',[])
    total=full.get('total',0)
    # Check the exact set of files, content hashes and statuses, not simply a claimed count.
    expected_demo = {('demo', p.stem.removesuffix('_demo')):p
                    for p in COURSE_ROOT.glob('03_HOC_PHAN/**/MA_MAU/*_demo.py')}
    expected_solution = {('solution',p.name.split('_bai_B_solution.py')[0]):p
                         for p in COURSE_ROOT.glob('31_HOAN_THIEN_LOI_GIAI_V28/*_bai_B_solution.py')}
    expected_paths={**expected_demo,**expected_solution}
    observed={(x.get('kind'),x.get('id')) for x in full_rows}
    issues=[]
    if len(expected_demo)!=441 or len(expected_solution)!=95:
        issues.append(f'Current archive files incomplete: demos={len(expected_demo)}, solutions={len(expected_solution)}')
    if len(full_rows)!=536 or total!=536 or len(observed)!=536:
        issues.append('Expected exactly 536 unique runtime reports')
    if observed != set(expected_paths):
        issues.append(f'Mismatch expected/observed tests: missing={len(set(expected_paths)-observed)}, extra={len(observed-set(expected_paths))}')
    for row in full_rows:
        key=(row.get('kind'),row.get('id'))
        path=expected_paths.get(key)
        if path is None: continue
        rel=path.relative_to(COURSE_ROOT).as_posix()
        if row.get('file') != rel:
            issues.append(f'Wrong path {key}');continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != row.get('sha256'):
            issues.append(f'Hash mismatch: {key}')
    states=collections.Counter(x.get('status') for x in full_rows)
    bad={k:v for k,v in states.items() if k not in ('PASS_EXIT_0','EXPECTED_ERROR')}
    expected_errors=[x for x in full_rows if x.get('status')=='EXPECTED_ERROR']
    if bad:issues.append(f'Unexpected statuses: {bad}')
    if len(expected_errors)!=1 or (expected_errors[0].get('kind'),expected_errors[0].get('id'))!=('demo','A04.02'):
        issues.append('Expected error is not exactly demo A04.02')
    full_problem='; '.join(issues[:6]) if issues else None
    core = bool(full_315 and deep_315 and not full_problem and not missing)
    tracks={k:rows.get(k,{}).get('status','NOT_RECORDED') for k in OPTIONAL_TRACKS}
    keras=json.loads(a.keras.read_text(encoding='utf8'))
    expected_keras_source=COURSE_ROOT/'tests/keras_torch_runtime_3152.py'
    versions=keras.get('versions', {})
    pip_check_text=a.pip_check.read_text(encoding='utf8').strip()
    keras_checks={
        'status': keras.get('status')=='KERAS_RUNTIME_PASS',
        'target_version': keras.get('python','').startswith('3.15.2 '),
        'backend': keras.get('backend')=='torch',
        'versions': all(versions.get(k)==v for k,v in {
            'keras':'3.15.1','torch':'2.15.0','h5py':'3.16.0','numpy':'2.5.4'}.items()),
        'source_sha256': (expected_keras_source.is_file() and
            hashlib.sha256(expected_keras_source.read_bytes()).hexdigest()==keras.get('source_sha256')),
        'wheel_sha256': (len(keras.get('h5py_wheel_sha256',''))==64 and
            all(c in '0123456789abcdef' for c in keras.get('h5py_wheel_sha256',''))),
        'pip_check': pip_check_text=='No broken requirements found.',
        'gradient': keras.get('gradient_observed')==[-4.0,0.0,6.0],
        'training': (isinstance(keras.get('initial_mse'),(float,int)) and
            isinstance(keras.get('final_mse'),(float,int)) and
            keras['initial_mse']>0 and keras['final_mse']<keras['initial_mse']*.05),
        'inference': (isinstance(keras.get('prediction_x3'),(float,int)) and
            abs(keras['prediction_x3']-7.0)<.3),
        'save_load': (isinstance(keras.get('prediction_after_reload'),(float,int)) and
            abs(keras['prediction_after_reload']-keras.get('prediction_x3',float('inf')))<1e-5),
    }
    keras_pass=all(keras_checks.values())
    report={'schema':'technical-audit-gate-v30',
        'target':'CPython 3.15.2',
        'full_suite_target_verified':full_315,
        'deep_suite_target_verified':deep_315,
        'full_suite_problem':full_problem,
        'missing_or_failing_mandatory_deep':missing,
        'core_cpu_technical_gate':'PASS' if core else 'NOT_PASSED',
        'additional_track_status':tracks,
        'keras_runtime_gate':'PASS' if keras_pass else 'NOT_PASSED',
        'keras_evidence_checks':keras_checks,
        'cpu_plus_keras_gate':'PASS' if core and keras_pass else 'NOT_PASSED',
        'global_professional_certification':'NOT_GRANTED_AUTOMATICALLY',
        'reason':'GPU/free-threading/native ABI need actual matching hardware/build; mathematical correctness, adversarial tests and external review cannot be proven by a smoke runner.'}
    a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'core_cpu_technical_gate':report['core_cpu_technical_gate'],
                     'additional_track_status':tracks,'output':str(a.output)},ensure_ascii=False))
    return 0 if core and keras_pass else 3

if __name__=='__main__':raise SystemExit(main())
