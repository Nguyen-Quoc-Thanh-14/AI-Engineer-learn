# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import numpy as np
scores=np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
mask=np.triu(np.ones((3,3),dtype=bool),1)
masked=np.where(mask,-np.inf,scores)
exp=np.exp(masked-masked.max(axis=1,keepdims=True));weights=exp/exp.sum(axis=1,keepdims=True)
assert np.allclose(weights.sum(axis=1),1.)
assert weights[0,1]==0 and weights[0,2]==0
assert weights[1,2]==0
print('PASS PN02.01')
