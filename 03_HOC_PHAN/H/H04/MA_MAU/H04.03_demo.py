# coding: utf-8
# Bài H04.03 — Tài liệu có thể thực thi độc lập
import random
r1 = random.Random(42)
r2 = random.Random(42)
assert [r1.randint(1,10) for _ in range(5)] == [r2.randint(1,10) for _ in range(5)]
