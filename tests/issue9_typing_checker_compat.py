"""Observe checker support for D06.03; do not lie about unsupported features."""
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence"/"issue9_content_qa"/"D06_03_checker_support.json"
POS=ROOT/"03_HOC_PHAN/D/D06/MA_MAU/D06.03_bai_B_typeform_fixture.py"
NEG=ROOT/"03_HOC_PHAN/D/D06/MA_MAU/D06.03_bai_B_typeform_negative.py"

def invoke(args):
    try:
        p=subprocess.run(args,capture_output=True,text=True,timeout=60,cwd=ROOT)
        return {"exit":p.returncode,"stdout":p.stdout[-1800:],"stderr":p.stderr[-1800:]}
    except (OSError,subprocess.TimeoutExpired) as exc:
        return {"exit":None,"error":type(exc).__name__+": "+str(exc)[:300]}

def run_checker(name,base):
    version=invoke([name,"--version"])
    positive=invoke([name,*base,str(POS)])
    negative=invoke([name,*base,str(NEG)])
    accepted=(positive.get("exit")==0 and isinstance(negative.get("exit"),int)
              and negative["exit"]!=0)
    return {"version":version,"positive":positive,"negative":negative,
            "status":"POSITIVE_ACCEPTED_NEGATIVE_REJECTED" if accepted
                     else "NOT_COMPATIBLE_OR_NOT_AVAILABLE"}

def main():
    if sys.version_info[:3]!=(3,15,2):
        print("REFUSE_WRONG_PYTHON",sys.version)
        return 2
    report={
        "lesson":"D06.03",
        "runtime":"CPython 3.15.2",
        "tool_status":{
            "mypy":run_checker("mypy",["--python-version","3.15","--show-error-codes"]),
            "pyright":run_checker("pyright",["--pythonversion","3.15"])
        },
        "gate":"CHECKER_PARITY_PENDING",
        "limits":"A positive+negative fixture demonstrates limited static checker support, not safe runtime parsing of untrusted inputs."
    }
    if all(v["status"]=="POSITIVE_ACCEPTED_NEGATIVE_REJECTED" for v in report["tool_status"].values()):
        report["gate"]="BOTH_CHECKERS_ACCEPT_FIXTURES"
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps({k:{"version":v["version"].get("stdout","")[:80],
                         "status":v["status"],
                         "positive_exit":v["positive"].get("exit"),
                         "negative_exit":v["negative"].get("exit")}
                      for k,v in report["tool_status"].items()},ensure_ascii=False))
    print("D06_03_CHECKER_GATE",report["gate"])
    return 0  # Report unsupported checkers explicitly; never claim full acceptance.

if __name__=="__main__":
    raise SystemExit(main())
