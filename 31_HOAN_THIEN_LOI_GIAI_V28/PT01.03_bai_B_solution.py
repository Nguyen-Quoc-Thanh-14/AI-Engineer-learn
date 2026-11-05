import numpy as np
A=np.array([[1.,2.],[2.,4.]])
s=np.linalg.svd(A,compute_uv=False)
assert s[0]>0 and s[1]<1e-12
assert np.linalg.matrix_rank(A)==1
