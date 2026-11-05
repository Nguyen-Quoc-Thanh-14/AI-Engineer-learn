# coding: utf-8
# Bài PV02.01 — Tài liệu có thể thực thi độc lập
import numpy as np,cv2
img=np.zeros((10,10),dtype=np.uint8)
img[:,5:]=255
edges=cv2.Canny(img,50,100)
assert edges.shape==img.shape
