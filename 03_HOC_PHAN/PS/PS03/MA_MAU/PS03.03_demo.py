# coding: utf-8
# Bài PS03.03 — Tài liệu có thể thực thi độc lập
import time
start=time.perf_counter();sum(range(1000));elapsed=time.perf_counter()-start
assert elapsed>=0
