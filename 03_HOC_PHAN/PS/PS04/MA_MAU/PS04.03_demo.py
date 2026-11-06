# coding: utf-8
# Bài PS04.03 — Tài liệu có thể thực thi độc lập
import numpy as np
a=np.arange(5.)
assert np.allclose(a*a,np.array([0,1,4,9,16]))
