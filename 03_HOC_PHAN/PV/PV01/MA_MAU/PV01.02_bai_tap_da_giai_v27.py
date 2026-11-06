# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import numpy as np
# Kênh RGB màu đỏ [255,0,0]; OpenCV thông dụng BGR [0,0,255].
rgb=np.array([[[255,0,0]]],dtype=np.uint8)
bgr=rgb[...,::-1].copy()
assert bgr.tolist()==[[[0,0,255]]]
assert bgr[...,::-1].tolist()==rgb.tolist()
assert bgr.shape==rgb.shape
print('PASS PV01.02')
