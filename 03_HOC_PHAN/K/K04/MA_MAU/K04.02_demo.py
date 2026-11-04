# coding: utf-8
# Bài K04.02 — Tài liệu có thể thực thi độc lập
def inner(x): return x*x
assert [inner(x) for x in (1,2,3)]==[1,4,9]
