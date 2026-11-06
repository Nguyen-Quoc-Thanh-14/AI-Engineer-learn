#!/usr/bin/env python3
"""Source-bound Issue #9 candidate categorization; never a semantic certification."""
import csv
import json
import re
from collections import Counter
from pathlib import Path
import issue9_content_inventory as inventory

OUT = inventory.OUT / "flagged_lesson_worklist.csv"
FIELDS = ("lesson_id", "part", "lesson_sha256", "answer_sha256", "demo_sha256",
          "candidate_flags", "review_queue", "evidence_status", "review_scope",
          "manual_expert_verification")

PRACTICAL = re.compile(
    r"(chạy|test|kiểm|thử|dựng|triển khai|benchmark|profiling|fuzz|"
    r"viết script|tạo module|viết C extension|so training|thực nghiệm)",
    re.IGNORECASE,
)

def classify(row):
    flags = set(filter(None, row["candidate_flags"].split(";")))
    if not flags:
        return None
    if "DESIGN_ANSWER_REVIEW" in flags:
        queue = ("RUNTIME_OR_TOOL_EVIDENCE_REQUIRED"
                 if PRACTICAL.search(row["B_prompt"]) else "DOCUMENT_DESIGN_REVIEW")
        scope = "Read actual B task, answer and linked reproducible evidence"
    elif "POSSIBLE_STALE_VERSION_CLAIM" in flags:
        queue = "VERIFY_HISTORICAL_B_SCOPE"
        scope = ("Historical 3.13.5 claim and lack of 3.15.2 direct B evidence; "
                 "536 demo/script CPU PASS does not imply this earlier B fixture ran")
    elif "ANSWER_NO_EMBEDDED_CODE_REVIEW" in flags:
        queue = "CHECK_LINKED_STANDALONE_B"
        scope = "B source exists externally; no Markdown code fence is not by itself an error"
    elif "ANSWER_SNIPPET_DIFFERS_FROM_B_SCRIPT_REVIEW" in flags:
        queue = "CHECK_ILLUSTRATION_VS_IMPLEMENTATION"
        scope = "AST differs; inspect task semantics, not necessarily a defect"
    else:
        queue = "MANUAL_TRIAGE"
        scope = "Inspect sources and determine whether the warning is a real defect"
    return {"lesson_id": row["lesson_id"], "part": row["part"],
            "lesson_sha256": row["lesson_sha256"], "answer_sha256": row["answer_sha256"],
            "demo_sha256": row["demo_sha256"], "candidate_flags": row["candidate_flags"],
            "review_queue": queue, "evidence_status": "UNVERIFIED_CANDIDATE",
            "review_scope": scope, "manual_expert_verification": "NOT_PERFORMED"}

def main():
    rows, errors = inventory.audit()
    if errors:
        raise RuntimeError(f"Source inventory failed: {errors[:5]}")
    flagged = [classify(r) for r in rows]
    flagged = [r for r in flagged if r]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(flagged)
    counts = dict(sorted(Counter(r["review_queue"] for r in flagged).items()))
    report = {
        "status": "SOURCE_BOUND_CANDIDATES_PENDING_MANUAL_CONTENT_REVIEW",
        "source_lessons": len(rows), "flagged_lessons": len(flagged),
        "candidate_counts": counts,
        "confirmed_defects_by_this_automated_worklist": 0,
        "external_expert_review": "NOT_PERFORMED",
        "limits": "Automated queue selection cannot verify semantic correctness or historical claims.",
    }
    (OUT.parent / "flag_review_summary.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
