# coding: utf-8
# Bài PS04.02 — Tài liệu có thể thực thi độc lập
import random,statistics
r=random.Random(9)
xs=[r.random() for _ in range(1000)]
assert abs(statistics.mean(xs)-.5)<.1
