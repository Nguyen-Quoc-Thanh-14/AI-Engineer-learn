# coding: utf-8
# Bài J03.02 — Tài liệu có thể thực thi độc lập
def squares(n):
    for i in range(n): yield i*i
g=squares(3)
assert next(g)==0
assert list(g)==[1,4]
assert list(g)==[]
