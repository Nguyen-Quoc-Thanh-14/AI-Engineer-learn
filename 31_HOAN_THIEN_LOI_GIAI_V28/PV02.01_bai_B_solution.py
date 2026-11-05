import numpy as np,cv2
img=np.zeros((60,60),dtype=np.uint8);cv2.rectangle(img,(15,15),(45,45),255,-1)
low=cv2.Canny(img,20,50);high=cv2.Canny(img,100,200)
assert np.count_nonzero(low)>0 and np.count_nonzero(high)>0
assert low.shape==high.shape==(60,60)
