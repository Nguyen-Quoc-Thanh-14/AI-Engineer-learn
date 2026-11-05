#!/usr/bin/env python3
"""Build unsigned human review assignments from current repository sources."""
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"evidence"/"expert_review_packets"
RISK=re.compile(r"^(?:N|L|PL|PM|PR)\d")
FIELDS=["assignment_id","lesson_id","part","slot","high_risk",
        "lesson_path","lesson_sha256","answer_path","answer_sha256",
        "demo_path","demo_sha256","solution_b_path","solution_b_sha256",
        "reviewer_github","review_evidence_url","state"]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def relative(root,p):
    return p.relative_to(root).as_posix()

def build(root=ROOT,expected=441):
    lessons=sorted((root/"03_HOC_PHAN").glob("**/BAI_HOC/*.md"))
    ids=[p.stem for p in lessons]
    if len(ids)!=expected or len(set(ids))!=expected:
        raise ValueError("Missing or duplicated lesson IDs")
    assignments=[]
    for lesson in lessons:
        k=lesson.stem
        part=lesson.relative_to(root/"03_HOC_PHAN").parts[0]
        chapter=lesson.parent.parent
        answer=chapter/"LOI_GIAI"/(k+"_loi_giai.md")
        demo=chapter/"MA_MAU"/(k+"_demo.py")
        solution=root/"31_HOAN_THIEN_LOI_GIAI_V28"/(k+"_bai_B_solution.py")
        for file in (lesson,answer,demo):
            if not file.is_file():
                raise ValueError(f"Missing required peer-review source: {file}")
        base=dict(lesson_id=k,part=part,high_risk="YES" if RISK.match(k) else "NO",
            lesson_path=relative(root,lesson),lesson_sha256=digest(lesson),
            answer_path=relative(root,answer),answer_sha256=digest(answer),
            demo_path=relative(root,demo),demo_sha256=digest(demo),
            solution_b_path=relative(root,solution) if solution.is_file() else "",
            solution_b_sha256=digest(solution) if solution.is_file() else "",
            reviewer_github="",review_evidence_url="",state="AWAITING_EXTERNAL_HUMAN")
        for slot in (1,2) if RISK.match(k) else (1,):
            assignments.append({"assignment_id":f"{k}-R{slot}",**base,"slot":slot})
    if len({r["assignment_id"] for r in assignments})!=len(assignments):
        raise ValueError("Repeated review slots")
    return assignments

def run():
    rows=build()
    high=sum(row["slot"]==2 for row in rows)
    if len(rows)!=520 or high!=79:
        raise ValueError(f"Wrong coverage: {len(rows)} assignments, {high} second reviews")
    OUT.mkdir(parents=True,exist_ok=True)
    with (OUT/"assignments.csv").open("w",newline="",encoding="utf8") as f:
        wr=csv.DictWriter(f,fieldnames=FIELDS)
        wr.writeheader()
        wr.writerows(rows)
    report={"lessons":441,"review_slots":len(rows),"high_risk_double_reviews":high,
        "slots_by_part":dict(sorted(Counter(r["part"] for r in rows).items())),
        "human_reviews_performed":0,
        "status":"ASSIGNMENTS_PREPARED_REVIEWERS_REQUIRED",
        "academic_certification":"NOT_GRANTED",
        "limitations":"No people invited or validated. No automatic expertise/identity/academic approval."}
    (OUT/"summary.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf8")
    print(json.dumps(report,ensure_ascii=False))
    return 0

if __name__=="__main__":
    raise SystemExit(run())
