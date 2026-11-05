# coding: utf-8
# Bài PS02.01 — Tài liệu có thể thực thi độc lập
import random
r=random.Random(42);n=2000
pi=4*sum(r.random()**2+r.random()**2<=1 for _ in range(n))/n
assert 2.5<pi<3.7
