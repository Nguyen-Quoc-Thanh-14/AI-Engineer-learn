# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import numpy as np
v=np.array([3.,4.]);axis=np.array([1.,0.])
projection=axis*np.dot(v,axis)/np.dot(axis,axis)
assert np.allclose(projection,[3,0])
assert np.isclose(np.linalg.norm(v),5)
assert np.isclose(np.linalg.norm(projection),3)
print('PASS PT01.02')
