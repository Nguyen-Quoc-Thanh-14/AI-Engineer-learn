# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import numpy as np
v=np.array([3.,4.]);axis=np.array([1.,0.])
projection=axis*np.dot(v,axis)/np.dot(axis,axis)
assert np.allclose(projection,[3,0])
assert np.isclose(np.linalg.norm(v),5)
assert np.isclose(np.linalg.norm(projection),3)
print('PASS PT01.02')
