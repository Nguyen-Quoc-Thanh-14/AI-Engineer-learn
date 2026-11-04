# coding: utf-8
# Bài PS01.02 — Tài liệu có thể thực thi độc lập
from scipy.optimize import brentq
root=brentq(lambda x:x*x-4,0,3)
assert abs(root-2)<1e-8
