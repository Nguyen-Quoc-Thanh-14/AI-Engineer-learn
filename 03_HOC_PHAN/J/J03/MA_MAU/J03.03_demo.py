# coding: utf-8
# Bài J03.03 — Tài liệu có thể thực thi độc lập
xs=[1,2,3]
a=[x*x for x in xs]
b=(x*x for x in xs)
assert a==[1,4,9]
assert list(b)==a
assert list(b)==[]
