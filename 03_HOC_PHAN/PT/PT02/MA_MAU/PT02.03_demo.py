# coding: utf-8
# Bài PT02.03 — Tài liệu có thể thực thi độc lập
import random
r=random.Random(3);x=[1,2,3]
bootstrap=[r.choice(x) for _ in x]
assert len(bootstrap)==3
