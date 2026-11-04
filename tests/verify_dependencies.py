"""Small CPU dependency checks; not a whole-curriculum or GPU proof."""
import json, pathlib, sys
assert sys.implementation.name == "cpython" and sys.version_info[:3] == (3, 15, 2)
results={}
def check(name,fn):
    try: results[name]={"status":"PASS","version":fn()}
    except Exception as exc: results[name]={"status":"FAIL","error":repr(exc)}
def check_numpy():
    import numpy as np
    assert float(np.array([1.,2.,3.]).mean()) == 2.
    return np.__version__
def check_pandas():
    import pandas as pd
    df=pd.DataFrame({"x":[1,2,3],"g":["a","a","b"]})
    assert df.groupby("g")["x"].sum().to_dict()=={"a":3,"b":3}
    return pd.__version__
def check_sklearn():
    import numpy as np, sklearn
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    x=np.array([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2]])
    y=[0,0,0,1,1,1]
    model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=300))
    model.fit(x,y)
    assert len(model.predict(x))==len(y)
    return sklearn.__version__
def check_torch():
    import torch
    x=torch.tensor([2.],requires_grad=True)
    (x*x).sum().backward()
    assert abs(x.grad.item()-4.)<1e-6
    return torch.__version__
def check_arrow():
    import io, pyarrow as pa, pyarrow.parquet as pq
    stream=io.BytesIO()
    pq.write_table(pa.table({"x":[1,2,3]}),stream)
    stream.seek(0)
    assert pq.read_table(stream).column("x").to_pylist()==[1,2,3]
    return pa.__version__
for name,fn in [("numpy",check_numpy),("pandas",check_pandas),
                ("scikit-learn",check_sklearn),("pytorch",check_torch),
                ("pyarrow",check_arrow)]:
    check(name,fn)
    print(name,results[name])
out=pathlib.Path(__file__).resolve().parents[1]/"evidence"/"cpu_dependencies.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"python":sys.version,"results":results},indent=2))
raise SystemExit(0 if all(x["status"]=="PASS" for x in results.values()) else 1)
