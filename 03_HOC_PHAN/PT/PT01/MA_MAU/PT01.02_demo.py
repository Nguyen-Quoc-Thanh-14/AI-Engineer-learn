# coding: utf-8
# Bài PT01.02 — Tài liệu có thể thực thi độc lập
import numpy as np
A=np.array([[1,2],[3,4]]);x=np.array([1,0])
assert (A@x).tolist()==[1,3]
