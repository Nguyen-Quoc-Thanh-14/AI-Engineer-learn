# coding: utf-8
# Bài PT03.01 — Tài liệu có thể thực thi độc lập
x=2.;h=1e-5
f=lambda x:(3*x+1)**2
approx=(f(x+h)-f(x-h))/(2*h)
assert abs(approx-6*(3*x+1))<1e-7
