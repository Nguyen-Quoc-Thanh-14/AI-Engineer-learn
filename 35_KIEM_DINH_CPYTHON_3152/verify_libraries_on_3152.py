#!/usr/bin/env python3
"""Functional package probes. CPython 3.15.2 only; no package installs."""
import sys,json,importlib.metadata,tempfile
if sys.implementation.name!='cpython' or sys.version_info[:3] != (3,15,2):
    print('BLOCKED: CPython 3.15.2 required')
    raise SystemExit(2)
results={}
def test(name,fn):
    try:
        fn();results[name]={'status':'PASS','version':importlib.metadata.version(name)}
    except ModuleNotFoundError as e:
        results[name]={'status':'NOT_INSTALLED','detail':str(e)}
    except Exception as e:
        results[name]={'status':'FAIL','detail':f'{type(e).__name__}: {e}'}

def numpy_test():
    import numpy as np
    x=np.array([1.,2.,3.]);assert np.isclose(x.mean(),2.)
    assert np.allclose(x*x,np.array([1.,4.,9.]))

def pandas_test():
    import pandas as pd
    assert int(pd.__version__.split('.')[0])>=3, 'need pandas >=3 for Copy-on-Write semantics'
    df=pd.DataFrame({'a':[1,2]});view=df[['a']];view.loc[0,'a']=999
    assert df.loc[0,'a']==1, 'Copy-on-Write regression'

def sklearn_test():
    import numpy as np
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score,StratifiedKFold
    x=np.array([[float(i),float(i*i)] for i in range(16)])
    y=np.array([0]*8+[1]*8)
    pipe=make_pipeline(StandardScaler(),LogisticRegression(max_iter=200))
    scores=cross_val_score(pipe,x,y,cv=StratifiedKFold(n_splits=4,shuffle=True,random_state=9))
    assert len(scores)==4 and scores.min()>=0.5

def torch_test():
    import torch
    x=torch.tensor([1.,2.,3.],requires_grad=True)
    (x*x).sum().backward()
    assert torch.allclose(x.grad,torch.tensor([2.,4.,6.]))

def arrow_test():
    import pyarrow as pa,pyarrow.parquet as pq
    from pathlib import Path
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'data.parquet';t=pa.table({'x':[1,2,3]})
        pq.write_table(t,p);t2=pq.read_table(p)
        assert t2.column('x').to_pylist()==[1,2,3]

def fastapi_test():
    from fastapi import FastAPI
    app=FastAPI()
    @app.get('/health')
    def health():return {'ok':True}
    assert len(app.routes)>=1

for name,fn in [('numpy',numpy_test),('pandas',pandas_test),('scikit-learn',sklearn_test),
                ('torch',torch_test),('pyarrow',arrow_test),('fastapi',fastapi_test)]:
    test(name,fn)
print(json.dumps({'runner':sys.version,'probes':results},ensure_ascii=False,indent=2))
raise SystemExit(int(any(item['status']=='FAIL' for item in results.values())))
