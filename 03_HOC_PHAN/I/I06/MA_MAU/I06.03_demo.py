# coding: utf-8
# Bài I06.03 — Tài liệu có thể thực thi độc lập
from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n<2: return n
    return fib(n-1)+fib(n-2)
assert fib(10)==55 and fib(0)==0
