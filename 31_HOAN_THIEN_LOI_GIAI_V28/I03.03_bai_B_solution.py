from collections import deque
import random,time,statistics
rng=random.Random(9)
for n in (100,10000):
    data=list(range(n));q=deque(data)
    ix=[rng.randrange(n) for _ in range(100)]
    assert [data[i] for i in ix]==[q[i] for i in ix]
    assert list(deque(data))==data
    # Semantics: deque.popleft is O(1); list.pop(0) is O(n) shifting elements.
    assert q.popleft()==0 and data.pop(0)==0
# Benchmarks require warmup/repetitions; asymptotic performance is not a fixed timing ratio.
