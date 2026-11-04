import numpy as np
A=np.array([[1.,1.],[1.,1.+1e-8]])
b=np.array([2.,2.+1e-8])
x=np.linalg.solve(A,b)
assert np.linalg.norm(A@x-b)<1e-8
assert np.linalg.cond(A)>1e7
