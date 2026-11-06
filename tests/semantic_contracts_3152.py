#!/usr/bin/env python3
"""Source-bound oracles and adversarial contract checks. Run on exact CPython 3.15.2.

This is a targeted enhancement, NOT a full formal proof of 441 lessons.
"""
from __future__ import annotations
import argparse, json, pathlib, runpy, subprocess, sys, tempfile, traceback

ROOT=pathlib.Path(__file__).resolve().parents[1]
EXPECTED_PATH=ROOT/'35_KIEM_DINH_CPYTHON_3152'/'ORACLE_RESULTS.json'

def check(label,fn,results):
    try:
        fn()
        results[label]={'status':'PASS'}
    except Exception as exc:
        results[label]={'status':'FAIL','error':f'{type(exc).__name__}: {exc}','traceback':traceback.format_exc(limit=3)}

def throws(fn,types=(ValueError,TypeError,UnicodeError)):
    try: fn()
    except types: return
    raise AssertionError('Invalid input incorrectly accepted')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--baseline',action='store_true')
    args=parser.parse_args()
    exact=(sys.implementation.name=='cpython' and sys.version_info[:3]==(3,15,2))
    if not (exact or args.baseline):
        print('BLOCKED: required exact CPython 3.15.2; use --baseline to run unvalidated local checks')
        return 2
    report={'runtime':sys.version, 'exact_3152':exact, 'status':'not_complete','tests':{}}
    tests=report['tests']
    rows=json.loads(EXPECTED_PATH.read_text(encoding='utf-8'))['results']
    assert len(rows)==17
    for row in rows:
        code=row['id'];source=list(ROOT.glob(f'03_HOC_PHAN/**/MA_MAU/{code}_demo.py'))
        if len(source)!=1:
            tests['oracle_'+code]={'status':'FAIL','error':'missing or ambiguous source path'}
            continue
        def verify(row=row,source=source[0]):
            with tempfile.TemporaryDirectory() as d:
                p=subprocess.run([sys.executable,'-I',str(source)],cwd=d,text=True,capture_output=True,timeout=20)
            assert p.returncode==0, f'exit {p.returncode}: {p.stderr[-700:]}'
            assert p.stdout.replace('\r\n','\n')==row['expected'].replace('\r\n','\n'), f'actual={p.stdout!r}; expected={row["expected"]!r}'
        check('oracle_'+code,verify,tests)
    # Source-bound adversarial tests. No arbitrary network, external process, or file write.
    def source(stem):
        matches=list(ROOT.glob(f'03_HOC_PHAN/**/MA_MAU/{stem}_demo.py'))
        assert len(matches)==1,stem
        return runpy.run_path(str(matches[0]))
    def solution(stem):
        matches=list(ROOT.glob(f'31_HOAN_THIEN_LOI_GIAI_V28/{stem}_bai_B_solution.py'))
        assert len(matches)==1,stem
        return runpy.run_path(str(matches[0]))
    def validate_untrusted():
        parse=solution('G03.03')['parse_untrusted']
        assert parse(b'{"quantity": 0}')==0
        assert parse(b'{"quantity": 1000}')==1000
        for v in (b'{"quantity": true}',b'{"quantity":-1}',b'{"quantity":1001}',
                  b'{"quantity":"100"}',b'{"quantity":1.0}',
                  b'{"quantity": 2, "admin": true}',b'null',b'[]',
                  b'{"quantity":1}; drop table',b' '*(4097)):
            throws(lambda v=v:parse(v))
    check('adversarial_G03.03_untrusted_JSON',validate_untrusted,tests)
    def thread_pool_test():
        jobs=source('L03.01')['run_jobs']
        assert jobs([])==[]
        assert jobs([0,-4,999])==[{'id':0,'value':0},{'id':-4,'value':-8},{'id':999,'value':1998}]
        for _ in range(4):
            inp=list(range(40))
            out=jobs(inp)
            assert out==[{'id':v,'value':v*2} for v in inp]
    check('boundary_L03.01_thread_pool',thread_pool_test,tests)
    def lazy_cache_test():
        fun=source('N03.01')['show_card']
        assert fun('cached',lambda:'fresh')=='fresh'
        def timeout(): raise TimeoutError()
        assert fun('cached',timeout)=='cached'
        throws(lambda:fun('cache',lambda: (_ for _ in ()).throw(ValueError())),(ValueError,))
    check('boundary_N03.01_timeout_fallback',lazy_cache_test,tests)
    def ctypes_test():
        d=source('PR01.01');ctypes=d['ctypes'];Point=d['Point']
        p=Point(-7,2**14)
        assert (p.x,p.y)==(-7,2**14)
        assert Point.x.offset==0 and Point.y.offset>=ctypes.sizeof(ctypes.c_int)
        assert ctypes.sizeof(Point)>=2*ctypes.sizeof(ctypes.c_int)
    check('boundary_PR01.01_ctypes_layout',ctypes_test,tests)
    def train_test_leakage_test():
        d=source('PM01.02')
        a=d['a'];b=d['b']
        assert len(a)==80 and len(b)==20
        assert sorted(a+b)==list(range(100))
        assert set(a).isdisjoint(b)
    check('boundary_PM01.02_disjoint_split',train_test_leakage_test,tests)
    from collections import Counter
    counts=Counter(v['status'] for v in tests.values())
    report['counts']=dict(counts)
    report['status']='PASS' if counts.get('FAIL',0)==0 and exact else ('BASELINE_ONLY' if counts.get('FAIL',0)==0 else 'FAIL')
    evidence=ROOT/'evidence'/'semantic_contracts_3152.json'
    evidence.parent.mkdir(exist_ok=True)
    evidence.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
    print('Target',sys.version.split()[0],'summary',report['counts'],'status',report['status'],'report',evidence)
    return int(counts.get('FAIL',0)>0 or not exact)

if __name__=='__main__':raise SystemExit(main())