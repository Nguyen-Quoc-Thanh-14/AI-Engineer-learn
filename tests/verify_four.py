"""Execute four unchanged course demos and assert expected output; persist evidence."""
import json
import pathlib
import subprocess
import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
CASES = {
 "C07.02": ("03_HOC_PHAN/C/C07/MA_MAU/C07.02_demo.py", ["3", "True"]),
 "C07.03": ("03_HOC_PHAN/C/C07/MA_MAU/C07.03_demo.py", ["False", "True"]),
 "C07.04": ("03_HOC_PHAN/C/C07/MA_MAU/C07.04_demo.py", ["[1, 2, 3, 4, 5]", "{'a': 1, 'b': 2}"]),
 "F05.02": ("03_HOC_PHAN/F/F05/MA_MAU/F05.02_demo.py", []),
}
def main():
    exact = sys.implementation.name == "cpython" and sys.version_info[:3] == (3, 15, 2)
    report = {"python": sys.version, "exact_runtime": exact, "scope": "FOUR original demos only", "results": {}}
    for lesson, (path, expected) in CASES.items():
        entry = {"path": path, "expected_stdout": expected}
        if not exact:
            entry["status"] = "BLOCKED_WRONG_RUNTIME"
        else:
            try:
                p = subprocess.run([sys.executable, "-I", str(ROOT / path)], capture_output=True, text=True, timeout=20)
                actual = p.stdout.strip().splitlines()
                entry.update(status="PASS" if p.returncode == 0 and actual == expected else "FAIL",
                             stdout=actual, stderr=p.stderr[-4000:], returncode=p.returncode)
            except subprocess.TimeoutExpired:
                entry["status"] = "TIMEOUT"
        report["results"][lesson] = entry
    out = ROOT / "evidence" / "four_demos.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    for key, value in report["results"].items():
        print(key, value["status"])
    return 0 if exact and all(v["status"] == "PASS" for v in report["results"].values()) else 1
if __name__ == "__main__":
    raise SystemExit(main())
