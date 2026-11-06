# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import ctypes
class Point(ctypes.Structure):
    _fields_=[('x',ctypes.c_int),('y',ctypes.c_int)]
p=Point(2,3)
assert p.x==2 and p.y==3
assert ctypes.sizeof(Point)>=2*ctypes.sizeof(ctypes.c_int)
print(p.x,p.y)
