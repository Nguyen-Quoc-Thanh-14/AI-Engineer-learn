# coding: utf-8
# Bài PS02.02 — Tài liệu có thể thực thi độc lập
import numpy as np
x=np.sin(2*np.pi*np.arange(8)/8)
f=np.fft.rfft(x)
assert len(f)==5
