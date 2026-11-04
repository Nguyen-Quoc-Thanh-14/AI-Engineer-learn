# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
def rgb_to_grayscale(pixel):
    if not isinstance(pixel, (tuple, list)) or len(pixel) != 3:
        raise ValueError('RGB cần 3 kênh')
    if any(type(v) is not int or not (0 <= v <= 255) for v in pixel):
        raise ValueError('mỗi kênh RGB phải là int từ 0 đến 255')
    r,g,b = pixel
    return round(0.299*r + 0.587*g + 0.114*b)

def check():
    assert rgb_to_grayscale((0,0,0)) == 0
    assert rgb_to_grayscale((255,255,255)) == 255
    assert rgb_to_grayscale((255,0,0)) == 76
    for bad in ((255, 0), (0,0,-1), (255,0,300), (True,0,0)):
        try: rgb_to_grayscale(bad)
        except ValueError: pass
        else: raise AssertionError('RGB sai')

if __name__ == '__main__':
    check()
    print('OK PV01.01')
