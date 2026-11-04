# coding: utf-8
# Bài PR01.03 — Tài liệu có thể thực thi độc lập
import ctypes
x=ctypes.c_int(3)
assert x.value==3 and ctypes.sizeof(x)>0
