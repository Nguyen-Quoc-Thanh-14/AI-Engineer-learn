#!/usr/bin/env python3
"""Fail-closed evidence audit, not a certificate of academic quality."""
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence"/"release_readiness_3152.json"
REPO=os.getenv("GITHUB_REPOSITORY","Nguyen-Quoc-Thanh-14/AI-Engineer-learn")
SHA=os.getenv("GITHUB_SHA","")
TOKEN=os.getenv("GH_TOKEN","")
WORKFLOWS={
    "cpu":"full-course-3152.yml",
    "semantic":"semantic-contracts-3152.yml",
    "structural":"curriculum-quality-audit.yml",
    "native":"course-native-pr02-3152.yml",
    "gpu":"gpu-self-hosted-3152.yml"}
ARTIFACTS={"cpu":"complete-cpython-3152-cpu-evidence",
           "gpu":"actual-cuda-cpython3152-evidence"}

def get_api(path):
    if not TOKEN:raise RuntimeError("Missing GitHub Actions read token")
    url="https://api.github.com/repos/"+REPO+"/"+path
    req=urllib.request.Request(url,headers={
        "Authorization":"Bearer "+TOKEN,
        "Accept":"application/vnd.github+json",
        "X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"course-release-readiness"})
    with urllib.request.urlopen(req,timeout=20) as reply:
        return json.load(reply)

def run():
    assert sys.implementation.name=="cpython" and sys.version_info[:3]==(3,15,2)
    OUT.parent.mkdir(exist_ok=True,parents=True)
    lessons=list(ROOT.glob("03_HOC_PHAN/**/BAI_HOC/*.md"))
    demos=list(ROOT.glob("03_HOC_PHAN/**/MA_MAU/*_demo.py"))
    solutions=list(ROOT.glob("31_HOAN_THIEN_LOI_GIAI_V28/*_bai_B_solution.py"))
    checks={"inventory":len(lessons)==441 and len(demos)==441
            and len({x.stem for x in lessons})==441
            and {x.stem for x in lessons}==
                {x.name.removesuffix("_demo.py") for x in demos}
            and len(solutions)==95,
            "sha_format":len(SHA)==40 and all(c in "0123456789abcdef" for c in SHA)}
    proofs={}
    errors=[]
    pr={}
    if checks["sha_format"] and TOKEN:
        try:
            candidate=get_api("actions/runs?head_sha="+SHA+"&per_page=100").get("workflow_runs",[])
            for group,file in WORKFLOWS.items():
                matched=[r for r in candidate if r.get("head_sha")==SHA
                         and str(r.get("path","")).split("@")[0].endswith("/"+file)
                         and r.get("conclusion")=="success" and r.get("status")=="completed"]
                if not matched:
                    proofs[group]={"passed":False,"reason":"NO_SUCCESS_ON_EXACT_SHA"}
                    continue
                latest=max(matched,key=lambda r:r.get("run_number",0))
                proof={"passed":True,"run_id":latest["id"],
                       "url":latest.get("html_url"),"sha":latest.get("head_sha")}
                if group in ARTIFACTS:
                    artifact_data=get_api("actions/runs/"+str(latest["id"])+"/artifacts?per_page=100")
                    found=[a for a in artifact_data.get("artifacts",[])
                           if a.get("name")==ARTIFACTS[group] and not a.get("expired",True)]
                    proof["passed"]=bool(found)
                    proof["artifact_id"]=found[0]["id"] if found else None
                proofs[group]=proof
            pull=get_api("pulls/4")
            pr={"draft":pull.get("draft"),"state":pull.get("state"),
                "merged":pull.get("merged",False),
                "head_sha":pull.get("head",{}).get("sha")}
            checks["pr_draft_unmerged"]=pr["draft"] is True and pr["state"]=="open" and not pr["merged"]
            checks["pr_sha_matches"]=pr["head_sha"]==SHA
        except Exception as exc:
            errors.append(type(exc).__name__+": "+str(exc)[:200])
    else:
        errors.append("Missing commit SHA or GitHub API credentials")
    for group in WORKFLOWS:
        checks["workflow_"+group]=proofs.get(group,{}).get("passed",False)
    reviewer=ROOT/"tests"/"independent_review_gate.py"
    if reviewer.is_file():
        try:
            proc=subprocess.run([sys.executable,str(reviewer)],cwd=ROOT,
                                capture_output=True,text=True,timeout=30)
            review=json.loads((ROOT/"evidence"/"independent_review_gate.json").read_text(encoding="utf8"))
            checks["review_manifest_complete"]=(
                proc.returncode==0 and
                review.get("review_manifest_state")=="RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK")
        except Exception as exc:
            review={"error":type(exc).__name__+": "+str(exc)}
            checks["review_manifest_complete"]=False
    else:
        review={"error":"Missing independent review checker"}
        checks["review_manifest_complete"]=False
    machine_ready=all(checks.values()) and not errors
    report={"status":"ELIGIBLE_FOR_HUMAN_FINAL_AUDIT" if machine_ready else "BLOCKED",
            "academic_certification":"NOT_GRANTED_AUTOMATICALLY",
            "runtime":sys.version,"sha":SHA,"checks":checks,
            "workflow_proofs":proofs,"pr":pr,"review":review,"errors":errors,
            "caveat":"Independent expertise, identity and reviewer findings require real human verification; an automatic passing status is not an academic certificate."}
    OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
    print(json.dumps({"status":report["status"],"sha":SHA,"checks":checks,"errors":errors},ensure_ascii=False))
    return 0 if machine_ready else 3

if __name__=="__main__":
    raise SystemExit(run())
