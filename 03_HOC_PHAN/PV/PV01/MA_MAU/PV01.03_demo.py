# coding: utf-8
# Bài PV01.03 — Tài liệu có thể thực thi độc lập
import numpy as np,cv2
x=np.zeros((5,5),dtype=np.uint8);x[2,2]=255
out=cv2.GaussianBlur(x,(3,3),0)
assert out.shape==x.shape
