# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import numpy as np
image=np.zeros((2,3,3),dtype=np.uint8)
image[0,1]=[255,0,0]
assert image.shape==(2,3,3)
assert image[0,1,0]==255
print(tuple(image[0,1]))
