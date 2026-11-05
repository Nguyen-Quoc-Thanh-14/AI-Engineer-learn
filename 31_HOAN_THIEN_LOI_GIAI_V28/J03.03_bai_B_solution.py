import tracemalloc
n=10000
tracemalloc.start()
gen=(i*i for i in range(n));a=tracemalloc.get_traced_memory()[0]
all_values=[i*i for i in range(n)];b=tracemalloc.get_traced_memory()[0]
assert sum(gen)==sum(all_values) and b>a
tracemalloc.stop()
# Memory includes interpreter overhead; repeat measurements before quantitative claims.
