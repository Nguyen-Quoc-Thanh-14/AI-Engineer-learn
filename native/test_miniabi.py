"""Test a single compiled abi3t .so on regular and GIL-disabled CPython 3.15.2."""
import importlib.machinery
import pathlib
import sys
import sysconfig
assert sys.implementation.name == "cpython"
assert sys.version_info[:3] == (3, 15, 2)
HERE = pathlib.Path(__file__).resolve().parent
assert (HERE / "miniabi.abi3t.so").is_file(), "missing abi3t .so"
assert ".abi3t.so" in importlib.machinery.EXTENSION_SUFFIXES
if sysconfig.get_config_var("Py_GIL_DISABLED"):
    assert hasattr(sys, "_is_gil_enabled") and not sys._is_gil_enabled()
sys.path.insert(0, str(HERE))
import miniabi
assert miniabi.twice(21) == 42
assert miniabi.twice(0) == 0
assert miniabi.twice(2**150) == 2**151
assert miniabi.twice(-7) == -14
assert miniabi.twice(1.5) == 3.0
try:
    miniabi.twice(object())
except TypeError:
    pass
else:
    raise AssertionError("object() multiplication should raise TypeError")
assert sys._is_gil_enabled() == (not bool(sysconfig.get_config_var("Py_GIL_DISABLED")))
print("PASS ABI3T import in", "free-threaded" if sysconfig.get_config_var("Py_GIL_DISABLED") else "normal", sys.version.split()[0])
