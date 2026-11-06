"""F05.02: probe eager vs explicit lazy imports on actual CPython 3.15.
Each case runs in an isolated subprocess with a fresh synthetic module.
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile

def run_probe(mode: str, *, fail_on_import: bool = False):
    if mode not in ("eager", "lazy_used", "lazy_unused"):
        raise ValueError("unsupported mode")
    if sys.implementation.name != "cpython" or sys.version_info[:2] != (3, 15):
        raise RuntimeError("F05.02 requires CPython 3.15")
    with tempfile.TemporaryDirectory(prefix="f0502_") as temp:
        module = Path(temp) / "side_effect_module.py"
        text = ("print('MODULE_INITIALIZED', flush=True)\n"
                + ("raise RuntimeError('synthetic import failure')\n"
                   if fail_on_import else "VALUE = 7\n"))
        module.write_text(text, encoding="utf8")
        statement = "import side_effect_module" if mode == "eager" else "lazy import side_effect_module"
        program = statement + "\nprint('MAIN_BEFORE', flush=True)\n"
        if mode != "lazy_unused":
            program += "print('VALUE', side_effect_module.VALUE, flush=True)\n"
        else:
            program += "print('MAIN_AFTER', flush=True)\n"
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        completed = subprocess.run(
            [sys.executable, "-c", program],
            cwd=temp, env=env, text=True, capture_output=True, timeout=15,
            check=False,
        )
        return {
            "stdout_lines": completed.stdout.splitlines(),
            "stderr": completed.stderr,
            "exit_code": completed.returncode,
        }

def verify():
    eager = run_probe("eager")
    lazy = run_probe("lazy_used")
    unused = run_probe("lazy_unused")
    assert eager["exit_code"] == lazy["exit_code"] == unused["exit_code"] == 0
    assert eager["stdout_lines"] == ["MODULE_INITIALIZED", "MAIN_BEFORE", "VALUE 7"], eager
    assert lazy["stdout_lines"] == ["MAIN_BEFORE", "MODULE_INITIALIZED", "VALUE 7"], lazy
    assert unused["stdout_lines"] == ["MAIN_BEFORE", "MAIN_AFTER"], unused
    return {"status": "F05_02_LAZY_IMPORT_PASS", "eager": eager["stdout_lines"],
            "lazy": lazy["stdout_lines"], "unused": unused["stdout_lines"]}

if __name__ == "__main__":
    print(verify())
