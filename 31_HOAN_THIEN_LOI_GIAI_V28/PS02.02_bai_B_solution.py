import numpy as np
fs=100;n=200;t=np.arange(n)/fs
slow=np.sin(2*np.pi*10*t)
above=np.sin(2*np.pi*90*t)
# 90 Hz sampled at 100 Hz aliases to 10 Hz (sign inversion).
assert np.allclose(above,-slow,atol=1e-12)
