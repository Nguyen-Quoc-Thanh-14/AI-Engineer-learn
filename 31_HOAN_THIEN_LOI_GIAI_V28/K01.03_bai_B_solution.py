import statistics,timeit
small=timeit.repeat('sum(range(100))',number=1,repeat=10)
large=timeit.repeat('sum(range(100))',number=1000,repeat=10)
assert len(small)==len(large)==10
assert statistics.median(large)>statistics.median(small)
print('median per execution',statistics.median(small),statistics.median(large)/1000)
# Compare medians per operation; don't claim hard speedup from noisy single runs.
