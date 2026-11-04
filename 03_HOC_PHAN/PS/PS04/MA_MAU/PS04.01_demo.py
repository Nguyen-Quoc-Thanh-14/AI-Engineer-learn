# coding: utf-8
# Bài PS04.01 — Tài liệu có thể thực thi độc lập
from scipy.optimize import root
r=root(lambda x:[x[0]**2-4],[3.])
assert r.success and abs(r.x[0]-2)<1e-7
