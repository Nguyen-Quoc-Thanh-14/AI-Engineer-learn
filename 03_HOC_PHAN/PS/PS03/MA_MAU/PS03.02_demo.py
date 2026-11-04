# coding: utf-8
# Bài PS03.02 — Tài liệu có thể thực thi độc lập
import ctypes
x=ctypes.c_int(7)
assert x.value==7 and ctypes.sizeof(x)>=2
