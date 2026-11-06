"""H05.01 B: independent real Ruff + Pyright positive/negative probes."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess

GOOD = """def double(value: int) -> int:
    return value * 2

assert double(4) == 8
"""
BAD = """import os
count: int = "bad type"
"""

def invoke(args):
    result = subprocess.run(args, capture_output=True, text=True, timeout=60)
    return {"exit": result.returncode, "output_tail": (result.stdout + "\n" + result.stderr)[-1100:]}

def check_quality_gates():
    with TemporaryDirectory(prefix="h0501_") as directory:
        root = Path(directory)
        good, bad = root/"good.py",root/"bad.py"
        good.write_text(GOOD, encoding="utf8")
        bad.write_text(BAD, encoding="utf8")
        results = {
            "ruff_good": invoke(["ruff","check",str(good)]),
            "ruff_bad": invoke(["ruff","check",str(bad)]),
            "pyright_good": invoke(["pyright","--pythonversion","3.15",str(good)]),
            "pyright_bad": invoke(["pyright","--pythonversion","3.15",str(bad)]),
        }
    passing = (results["ruff_good"]["exit"]==0 and results["ruff_bad"]["exit"]!=0
               and results["pyright_good"]["exit"]==0 and results["pyright_bad"]["exit"]!=0)
    return {"status":"QUALITY_GATES_PASS" if passing else "QUALITY_GATES_FAILED",
            "results":results,
            "ruff_version":invoke(["ruff","--version"])["output_tail"].strip(),
            "pyright_version":invoke(["pyright","--version"])["output_tail"].strip()}

if __name__ == "__main__":
    report = check_quality_gates()
    print(json.dumps(report,ensure_ascii=False))
    if report["status"] != "QUALITY_GATES_PASS":
        raise SystemExit(2)
    print("PASS H05.01")
