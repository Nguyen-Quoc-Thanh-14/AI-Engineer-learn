# coding: utf-8
# Bài K05.04 — Tài liệu có thể thực thi độc lập
from statistics import median
samples=[1.02,0.99,1.01,8.0]
assert abs(median(samples)-1.015)<1e-12
