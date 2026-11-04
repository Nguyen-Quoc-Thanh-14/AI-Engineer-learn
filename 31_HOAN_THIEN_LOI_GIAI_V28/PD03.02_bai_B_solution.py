import random,statistics

def bootstrap_ci(data,replications=400,seed=42):
    if not data:raise ValueError('empty')
    rng=random.Random(seed);n=len(data)
    means=sorted(statistics.mean(rng.choices(data,k=n)) for _ in range(replications))
    return means[int(.025*(replications-1))],means[int(.975*(replications-1))]
a,b=bootstrap_ci([1,2,3,4,5]);assert a<=3<=b
assert bootstrap_ci([2,2,2])==(2,2)
