# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import numpy as np
A=np.array([[1,2],[3,4]])
x=np.array([5,6])
y=A@x
assert y.tolist()==[17,39]
assert (x*x).tolist()==[25,36]
