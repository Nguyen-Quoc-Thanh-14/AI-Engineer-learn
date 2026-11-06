import numpy as np,time
x=np.arange(100000,dtype=np.float64)
a=[v*v for v in x];b=x*x
assert np.allclose(a,b)
# Run repeated wall-clock measurements separately and note vectorization may allocate intermediate arrays.
