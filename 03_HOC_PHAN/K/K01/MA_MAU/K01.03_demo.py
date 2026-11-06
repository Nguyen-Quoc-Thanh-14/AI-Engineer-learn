# coding: utf-8
# Bài K01.03 — Tài liệu có thể thực thi độc lập
import timeit
samples=timeit.repeat('sum(range(100))', repeat=3, number=1000)
assert len(samples)==3 and all(x>=0 for x in samples)
