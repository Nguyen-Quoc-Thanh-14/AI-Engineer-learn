# coding: utf-8
# Bài PN01.02 — Tài liệu có thể thực thi độc lập
import numpy as np
a=np.array([1.,0.]);b=np.array([0.9,0.1])
cos=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
assert .9<cos<=1
