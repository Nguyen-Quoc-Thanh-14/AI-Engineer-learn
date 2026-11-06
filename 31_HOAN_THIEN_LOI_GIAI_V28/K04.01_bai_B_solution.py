import numpy as np,time,tracemalloc
x=np.arange(1_000_000,dtype=np.float64)
vector=x*x
loop=np.array([v*v for v in x])
assert np.allclose(vector,loop)
# Timing and memory profile must be measured separately with repeat samples.
assert vector.nbytes==8_000_000
