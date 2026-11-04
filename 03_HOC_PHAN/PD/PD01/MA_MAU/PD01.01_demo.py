# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import numpy as np
x=np.array([[1,2,3],[4,5,6]],dtype=np.int64)
assert x.shape==(2,3)
assert x.dtype==np.dtype('int64')
assert x.sum(axis=0).tolist()==[5,7,9]
print(x.shape)
