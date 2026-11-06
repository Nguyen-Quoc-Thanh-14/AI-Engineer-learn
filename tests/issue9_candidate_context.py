#!/usr/bin/env python3
"""Read-only, source-bound Issue 9 triage context. NOT a semantic review."""
import json
import re
from pathlib import Path
import issue9_content_inventory as inventory

ROOT = inventory.ROOT
DEST = inventory.OUT / "candidate_context_3152.jsonl"
TITLE = re.compile(r"(?m)^#{1,4}\s+(.+)$")
FENCE = re.compile(r"(?m)^\x60\x60\x60(?:python|bash|sh|toml|json)?\s*$")

def main():
    rows, errors = inventory.audit()
    if errors:
        raise RuntimeError("Source inventory failures: " + repr(errors[:5]))
    records = []
    for row in rows:
        if not row["candidate_flags"]:
            continue
        answer = ROOT / row["answer_path"]
        lesson = ROOT / row["lesson_path"]
        body = answer.read_text(encoding="utf-8")
        prompt = row["B_prompt"]
        # Summarize source evidence only; no auto-ACCEPTED or invented reviewer.
        rec = {
            "id": row["lesson_id"], "part": row["part"],
            "flags": row["candidate_flags"].split(";"),
            "B_prompt": prompt,
            "answer_sha256": row["answer_sha256"],
            "lesson_sha256": row["lesson_sha256"],
            "answer_headings": TITLE.findall(body)[:12],
            "answer_excerpt": body[:1050],
            "answer_length_chars": len(body),
            "code_fence_lines": len(FENCE.findall(body)),
            "lesson_path": lesson.relative_to(ROOT).as_posix(),
            "answer_path": answer.relative_to(ROOT).as_posix(),
            "classification": "NEEDS_SOURCE_CONTENT_REVIEW",
            "not_expert_review": True
        }
        records.append(rec)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with DEST.open("w", encoding="utf-8") as fp:
        for rec in records:
            fp.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + chr(10))
    print("ISSUE9_CONTEXT_TOTAL", len(records), flush=True)
    for rec in records:
        # CI log gives an inspection queue, preserving source hash and wording.
        small = {k: rec[k] for k in ("id", "part", "flags", "B_prompt",
                                   "answer_headings", "answer_excerpt", "answer_sha256")}
        print("ISSUE9_CONTEXT " + json.dumps(small, ensure_ascii=False, separators=(",", ":")), flush=True)
    print("ISSUE9_CONTEXT_DONE; NO_AUTOMATIC_ACADEMIC_CERTIFICATION", flush=True)

if __name__ == "__main__":
    main()
