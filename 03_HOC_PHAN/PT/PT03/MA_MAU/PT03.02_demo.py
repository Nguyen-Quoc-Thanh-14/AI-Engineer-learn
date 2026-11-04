# coding: utf-8
# Bài PT03.02 — Tài liệu có thể thực thi độc lập
x=3.;lr=.1
for _ in range(50): x-=lr*(2*x)
assert abs(x)<.001
