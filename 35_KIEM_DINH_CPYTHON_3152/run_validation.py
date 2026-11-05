#!/usr/bin/env python3
"""Strict, reproducible smoke+assertion runner for a specified Python runtime.

Examples:
    python run_validation.py --suite all --strict --jobs 4
    python run_validation.py --suite all --baseline --jobs 4

--strict refuses anything other than CPython 3.15.2. No report of success
will be generated for an unsuitable runtime under strict mode.
"""
from __future__ import annotations
import argparse
import ast
import collections
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ERROR = {'A04.02': 'ZeroDivisionError'}
PY315_GATED = {'C07.02', 'C07.03', 'C07.04', 'F05.02'}
LIBRARIES = {
    'numpy': 'numpy', 'pandas': 'pandas', 'scikit-learn': 'sklearn',
    'torch': 'torch', 'pyarrow': 'pyarrow', 'tensorflow': 'tensorflow',
    'keras': 'keras', 'scipy': 'scipy', 'Pillow': 'PIL',
    'opencv-python': 'cv2', 'fastapi': 'fastapi',
    'SQLAlchemy': 'sqlalchemy', 'pytest': 'pytest',
}

def installed_libraries():
    result = {}
    for dist in LIBRARIES:
        try:
            result[dist] = importlib.metadata.version(dist)
        except importlib.metadata.PackageNotFoundError:
            result[dist] = None
    return result

def demo_cases():
    cases = []
    for p in sorted(ROOT.glob('03_HOC_PHAN/**/MA_MAU/*_demo.py')):
        key = p.stem.removesuffix('_demo')
        cases.append({'id':key,'kind':'demo','path':p})
    return cases

def solution_cases():
    # v2.8 contains 95 explicitly submitted B-solution scripts in this directory.
    return [{'id':p.name.split('_bai_B_solution.py')[0], 'kind':'solution', 'path':p}
            for p in sorted(ROOT.glob('31_HOAN_THIEN_LOI_GIAI_V28/*_bai_B_solution.py'))]

def one_case(case, timeout, version):
    p=case['path']; source=p.read_bytes()
    out={'id':case['id'],'kind':case['kind'], 'file':str(p.relative_to(ROOT)),
         'sha256':hashlib.sha256(source).hexdigest()}
    if case['id'] in PY315_GATED and version < (3,15):
        out.update(status='REQUIRES_PYTHON_315', elapsed_s=0.0,
                   detail='Blocked by features introduced in Python 3.15')
        return out
    start=time.perf_counter()
    try:
        # Temporary cwd + isolated mode + disabled user site. Runs no shell.
        with tempfile.TemporaryDirectory(prefix='py_course_audit_') as td:
            env=os.environ.copy()
            env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0',
                       OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                       OPENBLAS_NUM_THREADS='1', MPLBACKEND='Agg',
                       CUDA_VISIBLE_DEVICES='', TOKENIZERS_PARALLELISM='false')
            proc=subprocess.run([sys.executable,'-I',str(p)],cwd=td,
                                env=env,capture_output=True,text=True,
                                errors='replace', timeout=timeout)
        err=proc.stderr[-1200:]
        if proc.returncode==0:
            status='PASS_EXIT_0'
        elif case['kind']=='demo' and case['id'] in EXPECTED_ERROR and EXPECTED_ERROR[case['id']] in err:
            status='EXPECTED_ERROR'
        else:
            status='FAIL_EXIT'
        out.update(status=status, exit_code=proc.returncode,
                   stdout=proc.stdout[-1200:],stderr=err)
    except subprocess.TimeoutExpired:
        out.update(status='TIMEOUT',detail=f'exceeded {timeout}s')
    except Exception as e:
        out.update(status='HARNESS_ERROR',detail=f'{type(e).__name__}: {e}')
    out['elapsed_s']=round(time.perf_counter()-start,4)
    return out

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--strict',action='store_true',help='Require CPython 3.15.2 exactly')
    parser.add_argument('--baseline',action='store_true',help='Run on current Python without certifying 3.15.2')
    parser.add_argument('--suite',choices=('demos','solutions','all'),default='all')
    parser.add_argument('--jobs',type=int,default=4)
    parser.add_argument('--timeout',type=float,default=10.0)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('RUN_RESULT.json'))
    args=parser.parse_args()
    if args.strict==args.baseline:
        parser.error('Specify exactly one of --strict or --baseline')
    runtime=(sys.implementation.name, sys.version_info[:3])
    if args.strict and runtime != ('cpython',(3,15,2)):
        print(f'BLOCKED: expected CPython 3.15.2, got {sys.implementation.name} {sys.version.splitlines()[0]}', file=sys.stderr)
        raise SystemExit(2)
    cases=[]
    if args.suite in ('demos','all'):cases.extend(demo_cases())
    if args.suite in ('solutions','all'):cases.extend(solution_cases())
    if not cases:
        print('NO_CASES: missing expected curriculum source files', file=sys.stderr)
        raise SystemExit(3)
    records=[]
    with ThreadPoolExecutor(max_workers=max(1,min(args.jobs,8))) as pool:
        future_map={pool.submit(one_case,c,args.timeout,sys.version_info[:2]):c for c in cases}
        for fut in as_completed(future_map):
            records.append(fut.result())
            if len(records)%50==0:
                print(f'Processed {len(records)}/{len(cases)}',flush=True)
    records.sort(key=lambda x:(x['kind'],x['id']))
    count=collections.Counter(x['status'] for x in records)
    report={'schema':'course-validation-v29','runner':sys.version,'implementation':sys.implementation.name,
            'platform':platform.platform(),'strict_verified_runtime':args.strict,
            'test_semantics':'subprocess smoke tests; PASS_EXIT_0 is NOT a full functional assertion',
            'packages_installed':installed_libraries(), 'total':len(records),
            'status_counts':dict(sorted(count.items())),'results':records}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Saved',args.output,'runtime=',sys.version.splitlines()[0], 'results=',dict(count))
    blocked= {'FAIL_EXIT','TIMEOUT','HARNESS_ERROR'}
    if args.strict:blocked.add('REQUIRES_PYTHON_315')
    return int(any(x in count for x in blocked))

if __name__=='__main__':raise SystemExit(main())
