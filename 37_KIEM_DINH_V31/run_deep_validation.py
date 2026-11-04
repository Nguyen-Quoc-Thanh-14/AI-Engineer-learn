#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Evidence-driven tests. Strict mode refuses any interpreter other than CPython 3.15.2.
Run separately in regular and free-threaded CPython. Never silently upgrade SKIPs.
"""
from __future__ import annotations
import argparse, collections, hashlib, importlib.metadata, json, os
from pathlib import Path
import platform, subprocess, sys, tempfile, time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
TARGET=('cpython',(3,15,2))

def code_cases():
    return {
    'feature_frozendict': """from collections.abc import Mapping
x=frozendict({'a': 1, 'b': 2})
assert isinstance(x, Mapping)
assert not isinstance(x, dict)
assert x==frozendict({'b':2,'a':1})
assert hash(x)==hash(frozendict({'b':2,'a':1}))
try: x['a']=5
except TypeError: pass
else: raise AssertionError('frozendict must reject mutation')
try: hash(frozendict({'x': []}))
except TypeError: pass
else: raise AssertionError('unhashable nested value must be detected')
""",
    'feature_sentinel': """import copy
MISSING=sentinel('COURSE_MISSING')
d={'present_none':None,'zero':0}
assert d.get('present_none',MISSING) is None
assert d.get('not_present',MISSING) is MISSING
assert d.get('zero',MISSING)==0
assert copy.copy(MISSING) is MISSING
""",
    'feature_unpack_comprehension': """blocks=[[1,2],[],[3],[4,5]]
a=[*block for block in blocks]
assert a==[1,2,3,4,5]
entries=[{'a':1},{'b':2},{'a':3}]
d={**entry for entry in entries}
assert d=={'a':3,'b':2}
""",
    'feature_lazy_import': """import sys, tempfile
from pathlib import Path
_tmp=tempfile.TemporaryDirectory()
src=Path(_tmp.name)
marker=src/'LOADED'
module=src/'__audit_lazy_fixture_315.py'
module.write_text(chr(10).join(["from pathlib import Path", "Path("+repr(str(marker))+").write_text('loaded')", "VALUE = 73", ""]), encoding='utf8')
sys.path.insert(0,str(src))
lazy import __audit_lazy_fixture_315
assert not marker.exists(), 'module executed eagerly'
assert __audit_lazy_fixture_315.VALUE == 73
assert marker.read_text()=='loaded'
sys.path.pop(0)
_tmp.cleanup()
""",
    'library_numpy': """import numpy as np
x=np.array([1.,2.,3.]); y=np.array([3.,4.,5.])
assert np.allclose(x+y,[4.,6.,8.]); assert np.isclose(np.mean(x),2.)
""",
    'library_pandas_cow3': """import pandas as pd
from packaging.version import Version
assert Version(pd.__version__)>=Version('3.0'), 'Requires pandas >=3.0 CoW default'
df=pd.DataFrame({'v':[10,20]}); view=df[['v']]
df.loc[0,'v']=99
assert view.loc[0,'v']==10 and df.loc[0,'v']==99
""",
    'library_sklearn': """import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
X=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.],[2.,2.],[2.,3.]])
y=np.array([0,0,0,1,1,1])
m=make_pipeline(StandardScaler(), LogisticRegression(max_iter=300,random_state=42))
m.fit(X,y)
pred=m.predict(X)
assert pred.shape==(6,) and set(pred).issubset({0,1})
""",
    'library_torch_cpu': """import torch
x=torch.tensor([1.,2.,3.],requires_grad=True)
y=(x.square()).sum(); y.backward()
torch.testing.assert_close(x.grad,torch.tensor([2.,4.,6.]))
""",
    'library_pyarrow': """import pyarrow as pa
raw=pa.table({'id':[1,2],'value':['a','b']})
sink=pa.BufferOutputStream()
with pa.ipc.new_stream(sink,raw.schema) as writer: writer.write_table(raw)
read=pa.ipc.open_stream(sink.getvalue()).read_all()
assert read.equals(raw)
""",
    'library_scipy': """import numpy as np
from scipy.special import expit
assert np.isclose(expit(0.),0.5)
""",
    'library_pillow': """from PIL import Image
im=Image.new('RGB',(2,3),'white')
assert im.size==(2,3) and im.getpixel((0,0))==(255,255,255)
""",
    'library_opencv': """import cv2, numpy as np
x=np.zeros((3,3),np.uint8); x[1,1]=255
assert cv2.countNonZero(x)==1
""",
    'library_sqlalchemy': """from sqlalchemy import create_engine, text
engine=create_engine('sqlite+pysqlite:///:memory:')
with engine.begin() as conn:
    assert conn.execute(text('select 1+1')).scalar_one()==2
""",
    'library_fastapi': """from fastapi import FastAPI
app=FastAPI()
@app.get('/health')
def health():return {'ok':True}
assert len(app.routes)>0 and health()=={'ok':True}
""",
    'library_tensorflow': """import tensorflow as tf
x=tf.constant([1.,2.]); assert tf.reduce_sum(x).numpy()==3.0
""",
    'gpu_torch_cuda': """import torch
if not torch.cuda.is_available():
    print('SKIP_NO_CUDA_DEVICE'); raise SystemExit(77)
x=torch.tensor([1.,2.,3.],device='cuda',requires_grad=True)
y=(x*x).sum(); y.backward(); torch.cuda.synchronize()
torch.testing.assert_close(x.grad.cpu(),torch.tensor([2.,4.,6.]))
print('GPU',torch.cuda.get_device_name(0))
""",
    'free_threaded_no_gil': """import sys, sysconfig, threading
if sysconfig.get_config_var('Py_GIL_DISABLED') != 1:
    print('SKIP_NOT_FREE_THREADED_BUILD'); raise SystemExit(77)
if sys._is_gil_enabled():
    raise AssertionError('free-threaded build exists but GIL is currently enabled')
N=8; STEPS=2000; state={'n':0}; lock=threading.Lock()
def worker():
    for _ in range(STEPS):
        with lock:state['n']+=1
threads=[threading.Thread(target=worker) for _ in range(N)]
for thread in threads:thread.start()
for thread in threads:thread.join()
assert state['n']==N*STEPS
print('GIL_OFF_CONFIRMED')
""",
    }

LIBRARIES = {'library_numpy':'numpy','library_pandas_cow3':'pandas',
'library_sklearn':'scikit-learn','library_torch_cpu':'torch',
'library_pyarrow':'pyarrow','library_scipy':'scipy','library_pillow':'Pillow',
'library_opencv':'opencv-python','library_sqlalchemy':'SQLAlchemy',
'library_fastapi':'fastapi','library_tensorflow':'tensorflow'}

FEATURE_DEMOS={'C07.02':('3'+chr(10)+'True'+chr(10),'feature_frozendict'),
               'C07.03':('False'+chr(10)+'True'+chr(10),'feature_sentinel'),
               'C07.04':('[1, 2, 3, 4, 5]'+chr(10)+"{'a': 1, 'b': 2}"+chr(10),'feature_unpack_comprehension'),
               'F05.02':('','feature_lazy_import')}

def run_code(code,timeout,force_gil_off=False):
    with tempfile.TemporaryDirectory(prefix='course_v30_') as tmp:
        env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0',
             'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1',
             'MPLBACKEND':'Agg','TOKENIZERS_PARALLELISM':'false'}
        try:
            t=time.monotonic()
            res=subprocess.run([sys.executable,*(['-X','gil=0'] if force_gil_off else []),'-I','-c',code],cwd=tmp,env=env,
                        capture_output=True,text=True,errors='replace',timeout=timeout)
            return {'rc':res.returncode,'stdout':res.stdout[-1400:],'stderr':res.stderr[-1400:],
                    'elapsed_sec':round(time.monotonic()-t,3)}
        except subprocess.TimeoutExpired as exc:
            return {'rc':None,'stdout':'','stderr':str(exc),'elapsed_sec':timeout}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=['strict','baseline'],required=True)
    p.add_argument('--group',choices=['all','features','libraries','gpu','free','abi'],default='all')
    p.add_argument('--timeout',type=int,default=35)
    p.add_argument('--abi-module',default='',help='already installed compiled extension to audit')
    p.add_argument('--output',type=Path,default=HERE/'RUN_RESULTS_V30.json')
    args=p.parse_args()
    actual=(sys.implementation.name,tuple(sys.version_info[:3]))
    target=actual==TARGET
    if args.mode=='strict' and not target:
        print(f'BLOCKED: strict needs CPython 3.15.2, found {actual}',file=sys.stderr)
        return 2
    tests=code_cases(); names=[]
    if args.group in ('all','features'):
        names += ['feature_frozendict','feature_sentinel','feature_unpack_comprehension','feature_lazy_import']
    if args.group in ('all','libraries'):
        names += list(LIBRARIES)
    if args.group in ('all','gpu'): names+=['gpu_torch_cuda']
    if args.group in ('all','free'): names+=['free_threaded_no_gil']
    results=[]
    for name in names:
        record={'test':name,'sha256':hashlib.sha256(tests[name].encode()).hexdigest()}
        if name.startswith('feature_') and not target:
            record['status']='SKIP_NEEDS_CPYTHON_3152';results.append(record);continue
        package=LIBRARIES.get(name)
        if package:
            try: record['installed_version']=importlib.metadata.version(package)
            except importlib.metadata.PackageNotFoundError:
                record['status']='SKIP_DEPENDENCY_NOT_INSTALLED';results.append(record);continue
            if name=='library_pandas_cow3' and int(record['installed_version'].split('.')[0])<3:
                record['status']='SKIP_NEEDS_PANDAS_3';results.append(record);continue
        if name=='free_threaded_no_gil' and not target:
            record['status']='SKIP_NEEDS_CPYTHON_3152_FREE_BUILD';results.append(record);continue
        exec_result=run_code(tests[name], args.timeout, force_gil_off=(name=='free_threaded_no_gil'))
        record.update(exec_result)
        if record['rc']==0:record['status']='PASS_TARGET_3152' if target else 'PASS_BASELINE_ONLY'
        elif record['rc']==77:record['status']='SKIP_HARDWARE_OR_BUILD'
        elif record['rc'] is None:record['status']='TIMEOUT'
        else:record['status']='FAIL'
        results.append(record)
    if args.group in ('all','features'):
        for lesson,(expected,check) in FEATURE_DEMOS.items():
            r={'test':'original_'+lesson,'expected_output':expected,'related_semantic_check':check}
            path=next(ROOT.glob(f'03_HOC_PHAN/**/MA_MAU/{lesson}_demo.py'),None)
            if path is None:r['status']='FAIL_MISSING_DEMO'
            elif not target:r['status']='SKIP_NEEDS_CPYTHON_3152'
            else:
                with tempfile.TemporaryDirectory(prefix='course_orig_v30_') as tmp:
                    try:
                        resp=subprocess.run([sys.executable,'-I',str(path)],cwd=tmp,
                            capture_output=True,text=True,timeout=args.timeout)
                        r.update(returncode=resp.returncode, stdout=resp.stdout[-800:],stderr=resp.stderr[-800:])
                        r['status']='PASS_TARGET_3152' if resp.returncode==0 and resp.stdout==expected else 'FAIL'
                    except subprocess.TimeoutExpired:r['status']='TIMEOUT'
            results.append(r)
    if args.group in ('all','abi'):
        info={'test':'native_abi_compiled_extension','module':args.abi_module,
              'build_free_threaded':bool(__import__('sysconfig').get_config_var('Py_GIL_DISABLED')),
              'gil_enabled':sys._is_gil_enabled() if hasattr(sys,'_is_gil_enabled') else None}
        if not target:info['status']='SKIP_NEEDS_CPYTHON_3152'
        elif not args.abi_module:info['status']='SKIP_NEEDS_REAL_COMPILED_MODULE'
        else:
            source="import importlib,importlib.machinery,sys; m=importlib.import_module("+repr(args.abi_module)+"); p=m.__file__; assert any(p.endswith(s) for s in importlib.machinery.EXTENSION_SUFFIXES),p; print(p); print(sys._is_gil_enabled())"
            rr=run_code(source,args.timeout);info.update(rr)
            if rr['rc'] != 0:
                info['status']='FAIL_IMPORT_EXTENSION'
            else:
                module_path = rr.get('stdout','').splitlines()[0]
                after_import_gil = rr.get('stdout','').splitlines()[-1].strip() == 'True'
                info['extension_path']=module_path
                info['gil_after_import']=after_import_gil
                if info['build_free_threaded'] and after_import_gil:
                    info['status']='FAIL_EXTENSION_RE_ENABLED_GIL'
                elif info['build_free_threaded'] and '.abi3t.' in module_path and not after_import_gil:
                    info['status']='PASS_ABI3T_LOAD_TARGET'
                elif info['build_free_threaded']:
                    info['status']='NOT_PROVEN_ABI3T_TAG'
                else:
                    info['status']='PASS_REGULAR_EXTENSION_ONLY'
        results.append(info)
    report={'date_utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),
        'target_version':'CPython 3.15.2', 'interpreter':sys.version,
        'runtime_flags':{'abiflags':sys.abiflags,
                'Py_GIL_DISABLED':__import__('sysconfig').get_config_var('Py_GIL_DISABLED'),
                'gil_enabled':sys._is_gil_enabled() if hasattr(sys,'_is_gil_enabled') else None},
        'target_runtime_executed':target,'mode':args.mode,'group':args.group,
        'status_count':dict(collections.Counter(r['status'] for r in results)),
        'evidence_limit':'PASS checks the designated contract only, not full production safety; baseline is never a CPython 3.15.2 certification',
        'results':results}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({'target_runtime_executed':target,'status_count':report['status_count'],'output':str(args.output)},ensure_ascii=False))
    return int(any(r['status'].startswith('FAIL') or r['status']=='TIMEOUT' for r in results))

if __name__=='__main__':raise SystemExit(main())
