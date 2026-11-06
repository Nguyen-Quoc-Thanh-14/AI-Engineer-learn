# coding: utf-8
# Bài K02.03 — Tài liệu có thể thực thi độc lập
from array import array
from sys import getsizeof
xs=list(range(100))
a=array('i', xs)
assert list(a)==xs
assert getsizeof(a)>0
