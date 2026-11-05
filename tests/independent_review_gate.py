#!/usr/bin/env python3
"""Check proposed review records, never authenticate or impersonate reviewers."""
import csv
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "docs/review/INDEPENDENT_REVIEW_SIGNOFFS.csv"
OUT = ROOT / "evidence/independent_review_gate.json"
SCORE_FIELDS = ["technical_0_4", "pedagogy_0_4", "practical_0_4",
                "safety_0_4", "compatibility_0_4"]
FIELDS = ["lesson_id", "lesson_sha256", "answer_sha256", "demo_sha256",
          "solution_code_sha256", "reviewer_github", "reviewer_affiliation",
          "independence_declaration", "review_date_utc", *SCORE_FIELDS,
          "review_evidence_url", "adversarial_case_url", "findings_issue_urls",
          "fix_commit_sha", "retest_evidence_url", "decision"]
HIGH_RISK = re.compile(r"^(?:N|L|PM|PR|PL)\d")
LOGIN = re.compile(r"[a-z\d](?:[a-z\d-]{0,37}[a-z\d])?", re.I)
FORBIDDEN = {"nguyen-quoc-thanh-14", "chatgpt", "copilot", "ai", "bot"}


def filehash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def github_evidence_url(value):
    """Check URL syntax only; people must verify its author and actual contents."""
    try:
        p = urlsplit(value)
        return (p.scheme == "https" and p.netloc == "github.com"
                and not any(c.isspace() for c in value)
                and bool(re.fullmatch(
                    r"/[^/]+/[^/]+/(?:issues/[1-9]\d*|pull/[1-9]\d*"
                    r"|commit/[0-9a-f]{40}|actions/runs/[1-9]\d*"
                    r"|blob/[^/]+/.+)(?:/.*)?", p.path)))
    except (TypeError, ValueError):
        return False


def validate_records(root, records, *, expected_lessons=441, today=None):
    """Pure record validation; the small count override is for isolated fixtures."""
    today = today or datetime.now(timezone.utc).date()
    paths = list(root.glob("03_HOC_PHAN/**/BAI_HOC/*.md"))
    lessons = {p.stem: p for p in paths}
    errors = []
    if len(paths) != expected_lessons or len(lessons) != expected_lessons:
        errors.append(f"Expected {expected_lessons} unique lessons, found {len(paths)} files/{len(lessons)} IDs")
    accepted = {}
    seen = set()
    for line, rec in enumerate(records, 2):
        problem = lambda message: errors.append(f"row {line}: {message}")
        if set(rec) != set(FIELDS) or any(not isinstance(v, str) for v in rec.values()):
            problem("malformed CSV row or missing fields")
            continue
        k = rec["lesson_id"]
        if k not in lessons:
            problem("unknown lesson " + k)
            continue
        lesson = lessons[k]
        answer = lesson.parent.parent / "LOI_GIAI" / (k + "_loi_giai.md")
        demo = lesson.parent.parent / "MA_MAU" / (k + "_demo.py")
        code = root / "31_HOAN_THIEN_LOI_GIAI_V28" / (k + "_bai_B_solution.py")
        sources = {"lesson_sha256": lesson, "answer_sha256": answer, "demo_sha256": demo}
        if any(not p.is_file() or rec[field] != filehash(p) for field, p in sources.items()):
            problem("missing file or stale lesson/answer/demo checksum")
            continue
        if rec["solution_code_sha256"] != (filehash(code) if code.is_file() else ""):
            problem("stale standalone B solution checksum")
            continue
        reviewer = rec["reviewer_github"].strip().casefold()
        if not LOGIN.fullmatch(reviewer) or "--" in reviewer or reviewer in FORBIDDEN:
            problem("absent/invalid/author/AI reviewer")
            continue
        identity = (k, reviewer)
        if identity in seen:
            problem("duplicate reviewer for this lesson (GitHub logins are case-insensitive)")
            continue
        seen.add(identity)
        if not rec["reviewer_affiliation"].strip() or rec["independence_declaration"] != "CONFIRMED_NO_CONFLICT":
            problem("affiliation or conflict disclosure missing")
            continue
        try:
            text = rec["review_date_utc"]
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text) or date.fromisoformat(text) > today:
                raise ValueError("invalid or future date")
        except ValueError:
            problem("invalid or future review date")
            continue
        try:
            scores = [int(rec[key]) for key in SCORE_FIELDS]
            if any(v < 3 or v > 4 for v in scores):
                raise ValueError("score outside acceptance range")
        except ValueError:
            problem("scores must each be 3 or 4")
            continue
        if rec["decision"] != "ACCEPTED":
            problem("reviewer did not accept")
            continue
        if not all(github_evidence_url(rec[key]) for key in ("review_evidence_url", "adversarial_case_url")):
            problem("missing or malformed GitHub review/adversarial evidence URL")
            continue
        findings = rec["findings_issue_urls"].strip()
        if findings and not all(github_evidence_url(u) for u in re.split(r"[;\s]+", findings)):
            problem("malformed findings URLs")
            continue
        if findings or rec["fix_commit_sha"] or rec["retest_evidence_url"]:
            if not re.fullmatch(r"[0-9a-f]{40}", rec["fix_commit_sha"]) or not github_evidence_url(rec["retest_evidence_url"]):
                problem("findings/fix metadata require full fix SHA and retest evidence")
                continue
        accepted.setdefault(k, set()).add(reviewer)
    missing = sorted(set(lessons) - set(accepted))
    high_risk = sorted(k for k in lessons if HIGH_RISK.match(k) and len(accepted.get(k, ())) < 2)
    complete = not (missing or high_risk or errors)
    return {
        "source_lesson_count": len(paths), "review_rows_submitted": len(records),
        "lessons_with_machine_valid_review_evidence": len(accepted),
        "missing_lesson_ids_count": len(missing), "missing_ids_sample": missing[:20],
        "high_risk_lessons_requiring_second_review_count": len(high_risk),
        "problems_count": len(errors), "problems_sample": errors[:35],
        "review_manifest_state": "RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK" if complete else "EVIDENCE_PENDING",
        "academic_certification": "NOT_GRANTED_AUTOMATICALLY",
        "reviewer_identity_verification": "REQUIRES_HUMAN_VERIFICATION",
        "limits": "Hashes, CSV declarations and URL syntax cannot authenticate expertise, identity, independence, evidence contents or issue resolution. Human verification remains mandatory."
    }


def run():
    try:
        with CSV.open(encoding="utf8", newline="") as f:
            reader = csv.DictReader(f, strict=True)
            if reader.fieldnames != FIELDS:
                raise ValueError("Review signoff CSV header unexpectedly changed")
            records = list(reader)
        report = validate_records(ROOT, records)
    except (OSError, ValueError, csv.Error) as exc:
        report = {"review_manifest_state": "EVIDENCE_PENDING",
                  "academic_certification": "NOT_GRANTED_AUTOMATICALLY",
                  "problems_sample": [type(exc).__name__ + ": " + str(exc)]}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["review_manifest_state"] == "RECORDS_COMPLETE_NEEDS_HUMAN_IDENTITY_CHECK" else 3


if __name__ == "__main__":
    raise SystemExit(run())

