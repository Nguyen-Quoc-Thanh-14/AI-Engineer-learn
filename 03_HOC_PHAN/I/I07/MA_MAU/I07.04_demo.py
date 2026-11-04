# coding: utf-8
# Bài I07.04 — Tài liệu có thể thực thi độc lập
import random
r=random.Random(2026)
vals=[r.randrange(10) for _ in range(100)]
assert len(vals)==100 and all(0<=n<10 for n in vals)
