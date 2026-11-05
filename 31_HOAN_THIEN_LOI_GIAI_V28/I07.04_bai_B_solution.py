import random,collections
samples={seed:collections.Counter(random.Random(seed).randrange(10) for _ in range(1000)) for seed in (0,1,2)}
assert all(sum(counts.values())==1000 for counts in samples.values())
assert len({tuple(sorted(x.items())) for x in samples.values()})>1
# Distribution plausibility is NOT proof of RNG correctness or cryptographic security.
