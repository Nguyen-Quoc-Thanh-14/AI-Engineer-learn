"""Free-threaded interpreter smoke test. Does not prove extension ABI safety."""
import json, pathlib, sys, sysconfig, threading
from concurrent.futures import ThreadPoolExecutor
assert sys.implementation.name == "cpython" and sys.version_info[:3] == (3, 15, 2)
assert sysconfig.get_config_var("Py_GIL_DISABLED") == 1, "requires free-threaded build"
assert hasattr(sys, "_is_gil_enabled") and not sys._is_gil_enabled(), "GIL is not disabled"
value = [0]
lock = threading.Lock()
def worker(_):
    for n in range(1000):
        with lock:
            value[0] += 1
with ThreadPoolExecutor(max_workers=8) as pool:
    list(pool.map(worker, range(8)))
assert value[0] == 8000
out = pathlib.Path(__file__).resolve().parents[1] / "evidence" / "free_threading.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"status":"PASS", "version":sys.version, "GIL":False, "counter":value[0]}, indent=2))
print("PASS free threaded smoke check")
