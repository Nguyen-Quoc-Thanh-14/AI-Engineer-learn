"""Source-bound D06.02: both positive and negative static overload cases."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "03_HOC_PHAN/D/D06/MA_MAU/D06.02_bai_tap_da_giai_v27.py"
OUTPUT = ROOT / "evidence/issue9_content_qa/D06_02_static_checker_report.json"

def checked(argv):
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=90, cwd=ROOT)
        return {"exit": p.returncode, "out": (p.stdout + "\n" + p.stderr)[-2300:]}
    except (OSError, subprocess.TimeoutExpired) as e:
        return {"exit": None, "error": str(e)[:250]}

def main():
    if sys.implementation.name != "cpython" or sys.version_info[:3] != (3, 15, 2):
        raise RuntimeError("This CI fixture is required on CPython 3.15.2")
    source = SCRIPT.read_bytes()
    tree = ast.parse(source.decode("utf-8"))
    defs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "parse"]
    overloaded = [n for n in defs if any(isinstance(d, ast.Name) and d.id == "overload"
                                          for d in n.decorator_list)]
    imports = [n for n in tree.body if isinstance(n, ast.ImportFrom) and n.module == "typing"]
    if len(overloaded) != 2 or len(defs) != 3 or not imports:
        raise ValueError("B source must implement two overloads and one runtime function")
    source_derived = ast.unparse(ast.Module(body=[*imports, *defs], type_ignores=[]))
    tools = {
        "mypy": ["mypy", "--python-version", "3.15", "--show-error-codes"],
        "pyright": ["pyright", "--pythonversion", "3.15"]
    }
    with TemporaryDirectory(prefix="d0602_") as tmp:
        ok = Path(tmp) / "positive.py"
        bad = Path(tmp) / "negative.py"
        ok.write_text(source_derived + "\nx: int = parse(8)\ny: int = parse('8')\n", encoding="utf8")
        bad.write_text(source_derived + "\nx: int = parse([])\n", encoding="utf8")
        results = {}
        for name, command in tools.items():
            good = checked([*command, str(ok)])
            negative = checked([*command, str(bad)])
            passed = good["exit"] == 0 and negative["exit"] is not None and negative["exit"] != 0
            results[name] = {"positive": good, "negative": negative, "passed": passed}
    status = "STATIC_CHECKS_PASS" if all(z["passed"] for z in results.values()) else "STATIC_CHECKS_FAILED"
    report = {
        "status": status,
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "python": "3.15.2",
        "results": results,
        "limits": "Only checks the B source-derived overload signatures; it does not certify production safety or academic quality"
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(json.dumps({"status":status, "source_sha256":report["source_sha256"],
                      "exits":{k:[v["positive"]["exit"],v["negative"]["exit"]] for k,v in results.items()}},ensure_ascii=False))
    return 0 if status == "STATIC_CHECKS_PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
