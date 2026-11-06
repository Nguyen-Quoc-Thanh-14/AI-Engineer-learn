# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import numpy as np,cv2
image=np.zeros((5,5),dtype=np.uint8);image[2,2]=255
_,binary=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
dilated=cv2.dilate(binary,np.ones((3,3),dtype=np.uint8),iterations=1)
assert np.count_nonzero(binary)==1
assert np.count_nonzero(dilated)==9
assert dilated[2,2]==255
print('PASS PV01.03')
