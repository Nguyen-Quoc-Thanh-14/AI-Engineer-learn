"""PR02 native-course lab: import SAME compiled binary under both 3.15.2 runtimes."""
import importlib.machinery
import pathlib
import sys
import sysconfig

assert sys.implementation.name == "cpython" and sys.version_info[:3] == (3,15,2)
HERE=pathlib.Path(__file__).resolve().parent
assert (HERE/"course_math.abi3t.so").is_file()
assert ".abi3t.so" in importlib.machinery.EXTENSION_SUFFIXES
gil_disabled_build = sysconfig.get_config_var("Py_GIL_DISABLED") == 1
if gil_disabled_build:
    assert hasattr(sys,"_is_gil_enabled") and not sys._is_gil_enabled()
sys.path.insert(0,str(HERE))
import course_math
for v in (0,1,-1,2,-9,2**150,-(2**150)):
    assert course_math.cube_checked(v) == v**3
for bad in (None, "2", 1.5, [], {}):
    try: course_math.cube_checked(bad)
    except TypeError: pass
    else: raise AssertionError(f"Must reject {bad!r}")
if gil_disabled_build:
    assert not sys._is_gil_enabled(), "Import must not secretly enable GIL"
print("PASS course PR02 native module; free-threaded build=",gil_disabled_build)
