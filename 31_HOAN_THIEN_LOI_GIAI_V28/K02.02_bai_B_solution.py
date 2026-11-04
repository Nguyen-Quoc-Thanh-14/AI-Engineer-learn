import tracemalloc,gc
tracemalloc.start()
before=tracemalloc.take_snapshot()
a=[str(x) for x in range(10000)]
after=tracemalloc.take_snapshot()
changes=after.compare_to(before,'lineno')
assert changes and sum(x.size_diff for x in changes)>0
del a;gc.collect();tracemalloc.stop()
