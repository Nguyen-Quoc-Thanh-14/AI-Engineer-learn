"""Independent adversarial oracle for the actual N01.01 exercise on CPython 3.15.2."""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "03_HOC_PHAN/N/N01/MA_MAU/N01.01_bai_tap_da_giai_v25.py"
assert sys.implementation.name == "cpython" and sys.version_info[:3] == (3, 15, 2), sys.version

def invalid(func, x, expected_exc):
    try:
        func(x)
    except expected_exc:
        return
    raise AssertionError(f"Invalid input {repr(x)} was accepted")

def main():
    # This test is not imported by the lesson, so the oracle is independent from its assertions.
    parse_score = runpy.run_path(str(PATH))["parse_score"]
    passed = 0
    for x in [0, 1, 10, 2.25, 7.5, -0.0]:
        assert parse_score(x) == float(x)
        passed += 1
    for integer in range(-30, 41):
        if 0 <= integer <= 10:
            assert parse_score(integer) == float(integer)
        else:
            invalid(parse_score, integer, ValueError)
        passed += 1
    for x in [float("nan"), float("inf"), -float("inf"), -0.1, 10.00001, 10**500]:
        invalid(parse_score, x, ValueError)
        passed += 1
    for x in [True, False, "7", "", None, [], {}, b"7", complex(1,0)]:
        invalid(parse_score, x, TypeError)
        passed += 1
    assert math.isfinite(parse_score(9.999999))
    passed += 1
    out = ROOT / "evidence" / "highrisk_application_contracts.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "status": "PASS_SOURCE_BOUND_CONTRACT", "python": sys.version, "lesson": "N01.01",
        "source_path": PATH.relative_to(ROOT).as_posix(),
        "source_sha256": hashlib.sha256(PATH.read_bytes()).hexdigest(),
        "test_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "assertion_groups_count": passed,
        "scope": "score 0..10 NaN and invalid types only, not blanket pedagogy/security certification"
    }
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf8")
    print(json.dumps(report, ensure_ascii=False))
if __name__ == "__main__":
    main()
