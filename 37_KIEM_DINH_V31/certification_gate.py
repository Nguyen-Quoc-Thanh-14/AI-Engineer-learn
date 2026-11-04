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
    report={'schema':'technical-audit-gate-v30',
        'target':'CPython 3.15.2',
        'full_suite_target_verified':full_315,
        'deep_suite_target_verified':deep_315,
        'full_suite_problem':full_problem,
        'missing_or_failing_mandatory_deep':missing,
        'core_cpu_technical_gate':'PASS' if core else 'NOT_PASSED',
        'additional_track_status':tracks,
        'global_professional_certification':'NOT_GRANTED_AUTOMATICALLY',
        'reason':'GPU/free-threading/native ABI need actual matching hardware/build; mathematical correctness, adversarial tests and external review cannot be proven by a smoke runner.'}
    a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'core_cpu_technical_gate':report['core_cpu_technical_gate'],
                     'additional_track_status':tracks,'output':str(a.output)},ensure_ascii=False))
    return 0 if core else 3

if __name__=='__main__':raise SystemExit(main())
