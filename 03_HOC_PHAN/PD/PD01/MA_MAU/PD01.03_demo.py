# coding: utf-8
# Bài PD01.03 — Tài liệu có thể thực thi độc lập
import numpy as np
a=np.arange(8).reshape(2,4)
assert a.flags.c_contiguous and a.strides[1]==a.itemsize
