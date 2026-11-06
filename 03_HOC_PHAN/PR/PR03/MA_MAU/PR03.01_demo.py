# coding: utf-8
# Bài PR03.01 — Tài liệu có thể thực thi độc lập
from time import perf_counter
start=perf_counter();sum(range(10000))
assert perf_counter()-start>=0
