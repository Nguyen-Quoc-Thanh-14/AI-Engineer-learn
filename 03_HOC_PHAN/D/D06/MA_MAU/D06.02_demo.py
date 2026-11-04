# coding: utf-8
# Bài D06.02 — Tài liệu có thể thực thi độc lập
from typing import overload
@overload
def repeat(x:int)->int: ...
@overload
def repeat(x:str)->str: ...
def repeat(x): return x*2
assert repeat(2)==4 and repeat('a')=='aa'
