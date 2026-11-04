# coding: utf-8
# Bài PR01.04 — Tài liệu có thể thực thi độc lập
import timeit
samples=timeit.repeat('abs(-2)',repeat=2,number=1000)
assert min(samples)>=0
