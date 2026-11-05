#!/usr/bin/env python3
"""Validate proposed human-review evidence records; never impersonate a reviewer.

Even 441 complete records require separate human verification of credentials and
independence. No automatic global academic certification.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/"docs"/"review"/"INDEPENDENT_REVIEW_SIGNOFFS.csv"
OUT=ROOT/"evidence"/"independent_review_gate.json"
FIELDS=["lesson_id","lesson_sha256","answer_sha256","reviewer_github",
    "reviewer_affiliation","independence_declaration","review_date_utc",
    "technical_0_4","pedagogy_0_4","practical_0_4","safety_0_4",
    "compatibility_0_4","review_evidence_url","adversarial_case_url",
    "findings_issue_urls","fix_commit_sha","retest_evidence_url","decision"]
HIGH_RISK=("N","L","PM","PR","PL")

def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run():
    with CSV.open(encoding="utf8",newline="") as f:
        rdr=csv.DictReader(f)
        assert rdr.fieldnames==FIELDS, "Review signoff CSV header unexpectedly changed"
        records=list(rdr)
    lessons={p.stem:p for p in ROOT.glob("03_HOC_PHAN/**/BAI_HOC/*.md")}
    assert len(lessons)==441
    errors=[]
    accepted={}
    rows_by_lesson={}
    for i,rec in enumerate(records,2):
        k=rec.get("lesson_id","")
        if k not in lessons:
            errors.append("row "+str(i)+": unknown lesson "+k);continue
        p=lessons[k]
        sol=p.parent.parent/"LOI_GIAI"/(k+"_loi_giai.md")
        if rec["lesson_sha256"]!=filehash(p) or not sol.is_file() or rec["answer_sha256"]!=filehash(sol):
            errors.append("row "+str(i)+": stale source or solution checksum");continue
        reviewer=rec["reviewer_github"].strip()
        if not reviewer or reviewer.lower() in ("nguyen-quoc-thanh-14","chatgpt","copilot","ai","bot"):
            errors.append("row "+str(i)+": absent/author/AI reviewer not independent");continue
        if not rec["reviewer_affiliation"].strip() or rec["independence_declaration"]!="CONFIRMED_NO_CONFLICT":
            errors.append("row "+str(i)+": affiliation or conflict disclosure missing");continue
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}",rec["review_date_utc"]):
            errors.append("row "+str(i)+": missing review date");continue
        try: scores=[int(rec[key]) for key in FIELDS[7:12]]
        except (ValueError,TypeError):
            errors.append("row "+str(i)+": invalid score");continue
        if any(v<3 or v>4 for v in scores):
            errors.append("row "+str(i)+": score below acceptance threshold");continue
        if rec["decision"]!="ACCEPTED":
            errors.append("row "+str(i)+": reviewer did not accept");continue
        if not rec["review_evidence_url"].startswith("https://github.com/") or not rec["adversarial_case_url"].startswith("https://github.com/"):
            errors.append("row "+str(i)+": missing GitHub evidence/contract test");continue
        rows_by_lesson.setdefault(k,set()).add(reviewer)
        accepted[k]=True
    missing=sorted(set(lessons)-set(accepted))
    # High-risk lessons need two distinct, human-verified reviewers.
    high_risk_incomplete=sorted(k for k in lessons if k.startswith(HIGH_RISK) and len(rows_by_lesson.get(k,()))<2)
    report={
       "source_lesson_count":441,
       "review_rows_submitted":len(records),
       "lessons_with_machine_valid_review_evidence":len(accepted),
       "missing_lesson_ids_count":len(missing),
       "missing_ids_sample":missing[:20],
       "high_risk_lessons_requiring_second_review_count":len(high_risk_incomplete),
       "problems_sample":errors[:35],
       "review_manifest_state":"EVIDENCE_PENDING" if missing or errors or high_risk_incomplete else "RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK",
       "academic_certification":"NOT_GRANTED_AUTOMATICALLY",
       "limits":"CSV signatures and GitHub links can be falsified. Real credential, independence, content and issue resolution verification is a human obligation."
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf8")
    print(json.dumps(report,ensure_ascii=False))
    return 0 if not(missing or errors or high_risk_incomplete) else 3
if __name__=="__main__":raise SystemExit(run())
