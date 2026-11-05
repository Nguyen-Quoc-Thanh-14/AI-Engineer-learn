# coding: utf-8
# Bài K03.02 — Tài liệu có thể thực thi độc lập
from functools import lru_cache
@lru_cache(maxsize=64)
def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
assert fib(20)==6765
assert fib.cache_info().hits>0
