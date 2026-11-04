# coding: utf-8
# Bài K05.02 — Tài liệu có thể thực thi độc lập
import time
start=time.perf_counter();sum(i*i for i in range(10000))
assert time.perf_counter()>=start
