import numpy as np
A=np.array([[1.,1.],[1.,1.+1e-10]])
b=np.array([2.,2.+1e-10]);x=np.linalg.solve(A,b)
res=np.linalg.norm(A@x-b);cond=np.linalg.cond(A)
assert res<1e-9 and cond>1e9
# Small residual does not imply stable solution when the condition number is huge.
