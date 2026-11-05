#!/usr/bin/env python3
"""Independent CPython 3.15.2 functional oracles for five corrected exercises."""
import hashlib
import json
import math
from pathlib import Path
import runpy
import statistics
import sys

ROOT=Path(__file__).resolve().parents[1]
PARTS={"H02.01":"H/H02","PT03.01":"PT/PT03","PW01.01":"PW/PW01","K01.01":"K/K01","M04.01":"M/M04"}
assert sys.implementation.name=="cpython" and sys.version_info[:3]==(3,15,2),sys.version

def load(id):
    path=ROOT/"03_HOC_PHAN"/PARTS[id]/"MA_MAU"/(id+"_bai_tap_da_giai_v25.py")
    assert path.is_file(),path
    return runpy.run_path(str(path)),hashlib.sha256(path.read_bytes()).hexdigest()

def test_h(d):
    f=d["deduct_stock"]
    assert f(10,5)==5 and f(10,0)==10 and f(0,0)==0
    for qty in (-1,11):
        try:f(10,qty)
        except ValueError:pass
        else:raise AssertionError(qty)
    for qty in (True,"2"):
        try:f(10,qty)
        except TypeError:pass
        else:raise AssertionError(qty)
    # Ensure an actual independent unittest suite exists with 5 named cases.
    d["check"]()

def test_pt(d):
    grad=d["analytic_gradient"];numeric=d["finite_gradient"];f=d["f"]
    for x,y in ((0.,0.),(1.,2.),(-3.,4.),(2.5,-4.),(1e-2,7.)):
        assert math.isclose(f(x,y),x*x+3*x*y)
        wanted=(2*x+3*y,3*x)
        assert grad(x,y)==wanted
        actual=numeric(x,y)
        assert all(math.isclose(a,b,rel_tol=1e-8,abs_tol=1e-7) for a,b in zip(actual,wanted)),(x,y,wanted,actual)
    try:numeric(0,0,0)
    except ValueError:pass
    else:raise AssertionError("step 0")

def test_pw(d):
    mapping=d["public_http_error"]
    assert mapping(d["ValidationError"]("private field"))==(400,{"error":"Invalid input"})
    assert mapping(d["NotFoundError"]("missing 100"))==(404,{"error":"Not found"})
    secret="token=PRIVATE_AUTH_TOKEN"
    status,message=mapping(RuntimeError(secret))
    assert status==500
    assert secret not in json.dumps(message) and "Traceback" not in json.dumps(message)
    assert mapping(Exception("secret"))[0]==500

def test_k(d):
    a=d["squares_loop"];b=d["squares_comprehension"];measure=d["measure"]
    assert a(1000)==b(1000)
    for f in (a,b):
        r=measure(f,n=1000,repetitions=5,number=10)
        assert r["n"]==1000 and r["number"]==10
        assert len(r["samples"])==5 and all(x>=0 for x in r["samples"])
        assert math.isclose(r["median_seconds"],statistics.median(r["samples"]))
        assert math.isclose(r["range_seconds"],max(r["samples"])-min(r["samples"]))

def test_m(d):
    f=d["product_name"]
    with d["create_products_db"]() as conn:
        assert f(conn,1)=="Pen" and f(conn,2)=="Paper"
        assert f(conn,12345) is None
        for raw in ("1 OR 1=1", "1; DROP TABLE products", True):
            try:f(conn,raw)
            except TypeError:pass
            else:raise AssertionError("untrusted ID accepted")
        assert conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]==3

def main():
    checks={"H02.01":test_h,"PT03.01":test_pt,"PW01.01":test_pw,"K01.01":test_k,"M04.01":test_m}
    rows={}
    import traceback
    for code,check in checks.items():
        try:
            d,sha=load(code)
            check(d)
            rows[code]={"status":"PASS_TARGET_3152","sha256":sha}
        except Exception:
            rows[code]={"status":"FAIL","traceback":traceback.format_exc(limit=6)}
    result={"runtime":sys.version,"passed":sum(v["status"]=="PASS_TARGET_3152" for v in rows.values()),
            "total":len(rows),"results":rows,
            "limits":"Five exact exercise contracts, not whole-program peer review"}
    out=ROOT/"evidence"/"application_contracts_batch2_3152.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf8")
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["passed"]==result["total"] else 1
if __name__=="__main__":
    raise SystemExit(main())
