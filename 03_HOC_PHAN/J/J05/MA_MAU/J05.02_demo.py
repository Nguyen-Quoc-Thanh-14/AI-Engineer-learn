# coding: utf-8
# Bài J05.02 — Tài liệu có thể thực thi độc lập
import inspect
def f(a, *, b=3): return a+b
sig=inspect.signature(f)
assert 'b' in sig.parameters and f(2)==5
