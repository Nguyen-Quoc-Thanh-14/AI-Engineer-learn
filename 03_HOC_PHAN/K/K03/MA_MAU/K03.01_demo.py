# coding: utf-8
# Bài K03.01 — Tài liệu có thể thực thi độc lập
def squares(n):
    for i in range(n): yield i*i
assert sum(squares(5))==30
