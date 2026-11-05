import random,statistics,math
rng=random.Random(42);reps=[]
for _ in range(50):
    xs=[rng.random() for i in range(1000)];reps.append(statistics.mean(xs))
mean=statistics.mean(reps);se=statistics.stdev(reps)/math.sqrt(len(reps))
ci=(mean-1.96*se,mean+1.96*se)
assert ci[0]<.5<ci[1]
# Approximate 95% normal interval across replications; not a universal guarantee.
