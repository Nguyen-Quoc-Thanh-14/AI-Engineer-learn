"""PV01.01 corrected: 4x4 grayscale image with indexed diagonal."""
import numpy as np

def diagonal_image(size:int=4):
    if type(size) is not int or size<=0:raise ValueError("size positive int")
    image=np.zeros((size,size),dtype=np.uint8)
    indices=np.arange(size)
    image[indices,indices]=255
    return image

def check():
    image=diagonal_image()
    assert image.shape==(4,4) and image.dtype==np.uint8
    assert int(image.sum(dtype=np.int64))==1020
    assert np.all(np.diag(image)==255)
    assert np.count_nonzero(image)==4
    assert int(diagonal_image(1).sum())==255
    try:diagonal_image(0)
    except ValueError:pass
    else:raise AssertionError("empty image")
if __name__=="__main__":
    check()
    print("PASS PV01.01 grayscale 4x4 diagonal sum=1020")
