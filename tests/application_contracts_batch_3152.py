#!/usr/bin/env python3
"""Independent functional oracles for seven revised B-exercise answers, CPython 3.15.2."""
import bisect
import hashlib
import json
import math
from pathlib import Path
import runpy
import statistics
import sys
import traceback
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
PARTS={"I02.01":"I/I02","F01.01":"F/F01","PR01.01":"PR/PR01",
       "PN03.01":"PN/PN03","PS02.01":"PS/PS02",
       "PV01.01":"PV/PV01","PD01.01":"PD/PD01"}
assert sys.implementation.name=="cpython" and sys.version_info[:3]==(3,15,2), sys.version

def source(id):
    f=ROOT/"03_HOC_PHAN"/PARTS[id]/"MA_MAU"/(id+"_bai_tap_da_giai_v25.py")
    assert f.is_file(),f
    return runpy.run_path(str(f)), hashlib.sha256(f.read_bytes()).hexdigest()

def invalid(func,value,exception):
    try:func(value)
    except exception:return
    raise AssertionError("should reject "+repr(value))

def check_i(d):
    fun=d["lower_bound"]
    for seq in ([],[2],[2,2,2],[-3,0,0,7],list(range(-15,30,2))):
        for val in range(-20,35):
            assert fun(seq,val)==bisect.bisect_left(seq,val)
    assert fun([1,3,5],4)==2 and fun([],2)==0

def check_f(d):
    fun=d["nonempty_mean"]
    for arr in ([1,2,3],[-1,3],[-5.2,1.1,10.9],[0],list(range(10))):
        assert abs(fun(arr)-statistics.mean(arr))<1e-10
    for bad in ([],[float("nan")],[float("inf")],[True,2],["1",2]):
        invalid(fun,bad,ValueError)
    invalid(fun,(1,2),TypeError)

def check_pr(d):
    import ctypes
    Point=d["Point"];report=d["layout"]()
    assert report["size"]==ctypes.sizeof(Point)
    assert report["alignment"]==ctypes.alignment(Point)
    assert report["y_offset"]==Point.y.offset
    assert Point.y.offset%ctypes.alignment(ctypes.c_double)==0
    assert Point.x.offset==0
    assert ctypes.sizeof(Point)>=Point.y.offset+ctypes.sizeof(ctypes.c_double)

def check_pn(d):
    rows=d["build_evaluation_set"]()
    assert len(rows)==30
    assert len({r["id"] for r in rows})==30
    assert sum(r["expected"]=="grounded" for r in rows)==15
    assert sum(r["expected"]=="unsupported" for r in rows)==15
    for r in rows:
        assert r["question"] and r["reference_answer"] and r["evidence"]
        assert d["classify_text_support"](r["evidence"],r["candidate_answer"])==r["expected"]
    invalid(lambda x:d["classify_text_support"]("context",x),"",ValueError)

def check_ps(d):
    fun=d["estimate_pi"]; rows=d["compare_sample_sizes"]((100,1000,5000),runs=10)
    assert len(rows)==3 and all(r["runs"]==10 for r in rows)
    assert all(0<=r["mean_pi"]<=4 and r["half_width_95pct_normal_approx"]>=0 for r in rows)
    assert abs(rows[-1]["mean_pi"]-math.pi)<0.12
    xml=d["render_error_bars_svg"](rows)
    root=ET.fromstring(xml)
    assert root.tag.endswith("svg")
    assert len([x for x in root if x.tag.endswith("circle")])==3
    invalid(lambda v:fun(v,7),0,ValueError)
    invalid(lambda v:fun(v,7),True,ValueError)

def check_pv(d):
    import numpy as np
    fun=d["diagonal_image"]
    out=fun(4)
    assert out.shape==(4,4) and out.dtype==np.uint8
    assert int(out.sum(dtype=np.int64))==4*255
    assert np.array_equal(out,np.eye(4,dtype=np.uint8)*255)
    assert np.array_equal(fun(1),np.array([[255]],dtype=np.uint8))
    invalid(fun,-1,ValueError)

def check_pd(d):
    import numpy as np
    x,view,copied=d["view_vs_copy"]()
    assert x.shape==(4,3) and view.shape==(4,) and np.shares_memory(view,x)
    assert x[0,1]==999 and copied[0]==-42
    assert not np.shares_memory(copied,x)
    assert np.empty((0,3))[:,1].shape==(0,)

def main():
    checks={"I02.01":check_i,"F01.01":check_f,"PR01.01":check_pr,
            "PN03.01":check_pn,"PS02.01":check_ps,
            "PV01.01":check_pv,"PD01.01":check_pd}
    result={"python":sys.version,"cases":{}}
    for id,check in checks.items():
        try:
            d,source_hash=source(id)
            check(d)
            result["cases"][id]={"status":"PASS_TARGET_3152","source_sha256":source_hash}
        except Exception:
            result["cases"][id]={"status":"FAIL","traceback":traceback.format_exc(limit=7)}
    result["passed"]=sum(x["status"]=="PASS_TARGET_3152" for x in result["cases"].values())
    result["total"]=len(checks)
    result["scope"]="7 source-bound B application contracts; NOT all 441 solutions independently reviewed"
    out=ROOT/"evidence"/"application_contracts_batch_3152.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf8")
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["passed"]==result["total"] else 1
if __name__=="__main__":
    raise SystemExit(main())
