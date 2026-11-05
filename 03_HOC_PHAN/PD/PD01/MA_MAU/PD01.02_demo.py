# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import numpy as np
x=np.array([[1,2,3],[4,5,6]])
v=np.array([10,20,30])
y=x+v
assert y.tolist()==[[11,22,33],[14,25,36]]
assert y.shape==(2,3)
