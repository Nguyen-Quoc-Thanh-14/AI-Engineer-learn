#!/usr/bin/env python3
"""Execute historical B (v27) scripts tied to source-flagged lessons, without claiming full semantic review.

Each B script must exit 0 and emit an exact PASS <lesson_id> marker on CPython 3.15.2.
A script absent from the repository is explicitly recorded, never marked PASS.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import issue9_content_inventory as inv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence" / "issue9_content_qa" / "historical_B_3152_probe.json"

def hash_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inspect():
    if sys.implementation.name != "cpython" or sys.version_info[:3] != (3, 15, 2):
        raise RuntimeError("Requires CPython 3.15.2")
    lesson_rows, structural_errors = inv.audit()
    if structural_errors:
        raise RuntimeError("Invalid source inventory: " + str(structural_errors[:5]))
    suspects = [r for r in lesson_rows if
                "POSSIBLE_STALE_VERSION_CLAIM" in r["candidate_flags"].split(";")]
    outputs = []
    for row in suspects:
        identifier = row["lesson_id"]
        lesson_path = ROOT / row["lesson_path"]
        chapter = lesson_path.parent.parent
        script = chapter / "MA_MAU" / (identifier + "_bai_tap_da_giai_v27.py")
        if not script.exists():
            outputs.append({"id": identifier, "status": "NO_HISTORICAL_B_SCRIPT",
                            "lesson_sha256": row["lesson_sha256"]})
            continue
        start = time.monotonic()
        with tempfile.TemporaryDirectory(prefix="b_3152_") as temp:
            env = {
                "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                "HOME": temp, "TMPDIR": temp, "PYTHONDONTWRITEBYTECODE": "1",
                "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
                "MKL_NUM_THREADS": "1",
            }
            try:
                proc = subprocess.run(
                    [sys.executable, "-I", str(script.resolve())],
                    cwd=temp, env=env, capture_output=True, text=True,
                    timeout=35, check=False
                )
                marker = "PASS " + identifier
                status = ("B_SCRIPT_3152_PASS" if proc.returncode == 0
                          and marker in proc.stdout.splitlines() else "B_SCRIPT_FAILED")
                result = {
                    "id": identifier, "status": status,
                    "exit_code": proc.returncode,
                    "expected_marker": marker,
                    "stdout_tail": proc.stdout[-1500:],
                    "stderr_tail": proc.stderr[-1500:],
                }
            except subprocess.TimeoutExpired:
                result = {"id": identifier, "status": "B_SCRIPT_TIMEOUT"}
        result["duration_seconds"] = round(time.monotonic() - start, 3)
        result["script"] = script.relative_to(ROOT).as_posix()
        result["script_sha256"] = hash_file(script)
        result["lesson_sha256"] = row["lesson_sha256"]
        outputs.append(result)
        print(identifier, result["status"], flush=True)
    statuses = {s: sum(x["status"] == s for x in outputs)
                for s in sorted({r["status"] for r in outputs})}
    report = {
        "status": "SOURCE_BOUND_HISTORICAL_B_RUNTIME_PROBE",
        "source_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "python_version": ".".join(map(str, sys.version_info[:3])),
        "candidate_count": len(suspects),
        "status_counts": statuses,
        "results": outputs,
        "full_expert_review": False,
        "limitations": ("Exec exit 0 + a PASS marker proves a particular script ran to completion, "
                        "not its pedagogical correctness. Missing historical B scripts stay unverified. "
                        "This is not the 536-script core suite."),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf8")
    print(json.dumps({k:v for k,v in report.items() if k!="results"},ensure_ascii=False))
    return 0 if statuses.get("B_SCRIPT_FAILED", 0) == 0 and statuses.get("B_SCRIPT_TIMEOUT", 0) == 0 else 2

if __name__ == "__main__":
    raise SystemExit(inspect())
