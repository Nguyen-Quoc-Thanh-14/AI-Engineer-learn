import sys,platform,threading
from concurrent.futures import ThreadPoolExecutor

def cpu_sum(n):return sum(i*i for i in range(n))
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(cpu_sum,[1000,1000]))
assert results==[cpu_sum(1000)]*2
print(platform.python_implementation(),sys.version.split()[0])
print('GIL enabled?',getattr(sys,'_is_gil_enabled',lambda:'unknown')())
# No throughput claims from this correctness-only test; require a CPython free-threaded build for comparison.
