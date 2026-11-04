import random,statistics
rng=random.Random(7);data=[1,2,3,4,5,6,7]
medians=sorted(statistics.median(rng.choices(data,k=len(data))) for _ in range(1000))
lo,hi=medians[24],medians[974]
assert lo<=statistics.median(data)<=hi
