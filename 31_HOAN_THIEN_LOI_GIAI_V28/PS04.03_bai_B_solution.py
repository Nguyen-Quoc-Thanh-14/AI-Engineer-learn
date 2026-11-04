import numpy as np
try:
    from numba import njit
except ImportError: njit=None
x=np.arange(1000,dtype=np.float64)
ref=np.square(x).sum()
if njit is not None:
    @njit
    def squares(x):
        total=0.
        for v in x:total+=v*v
        return total
    assert np.isclose(squares(x),ref)
    # The first call also compiles the kernel: benchmark steady-state after warmup.
