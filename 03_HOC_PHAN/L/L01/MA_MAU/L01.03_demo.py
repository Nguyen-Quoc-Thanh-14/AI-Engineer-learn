# coding: utf-8
# Bài L01.03 — Tài liệu có thể thực thi độc lập
from time import perf_counter
start=perf_counter()
result=sum(i*i for i in range(10000))
assert result>0 and perf_counter()-start>=0
