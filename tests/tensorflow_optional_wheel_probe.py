#!/usr/bin/env python3
"""Optional TensorFlow CPython 3.15 binary-wheel resolution check.
A successful workflow means the probe executed, NOT that TensorFlow runtime passed.
"""
import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence" / "tensorflow_optional" / "wheel_resolution_3152.json"

def main():
    assert sys.implementation.name == "cpython" and sys.version_info[:3] == (3, 15, 2)
    command = [
        sys.executable, "-m", "pip", "install", "--dry-run",
        "--no-deps", "--only-binary=:all:", "--no-cache-dir", "tensorflow",
    ]
    outcome = {
        "python_version": platform.python_version(), "platform": platform.platform(),
        "probe": "pip install --dry-run --no-deps --only-binary=:all: tensorflow",
        "runtime_executed": False, "tensorflow_runtime_verified": False,
    }
    try:
        p = subprocess.run(command, capture_output=True, text=True, timeout=180, check=False)
        output = (p.stdout + "\n" + p.stderr)[-12000:]
        outcome["pip_exit_code"] = p.returncode
        outcome["resolver_output_tail"] = output
        if p.returncode == 0:
            outcome["status"] = "BINARY_WHEEL_RESOLVABLE_RUNTIME_UNTESTED"
        elif "No matching distribution found for tensorflow" in output:
            outcome["status"] = "NO_COMPATIBLE_BINARY_WHEEL_FOUND"
        else:
            outcome["status"] = "RESOLUTION_INCONCLUSIVE"
    except subprocess.TimeoutExpired:
        outcome["status"] = "RESOLUTION_TIMEOUT"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(outcome, ensure_ascii=False, indent=2)+"\n", encoding="utf8")
    print(json.dumps({k:v for k,v in outcome.items() if k!="resolver_output_tail"}))
    return 0 if outcome["status"] in (
        "BINARY_WHEEL_RESOLVABLE_RUNTIME_UNTESTED", "NO_COMPATIBLE_BINARY_WHEEL_FOUND"
    ) else 2

if __name__ == "__main__":
    raise SystemExit(main())
