# coding: utf-8
# Bài PL03.03 — Tài liệu có thể thực thi độc lập
import random
r=random.Random(1)
sequence=[r.choice(['A','B']) for _ in range(5)]
assert len(sequence)==5
