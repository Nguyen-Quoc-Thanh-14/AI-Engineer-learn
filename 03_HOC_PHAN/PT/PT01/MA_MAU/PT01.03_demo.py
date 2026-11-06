# coding: utf-8
# Bài PT01.03 — Tài liệu có thể thực thi độc lập
import numpy as np
A=np.array([[3.,0.],[0.,2.]])
u,s,vt=np.linalg.svd(A)
assert np.allclose((u*s)@vt,A)
