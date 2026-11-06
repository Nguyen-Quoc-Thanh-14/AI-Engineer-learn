# coding: utf-8
# Bài H06.01 — Tài liệu có thể thực thi độc lập
from collections import Counter
for xs in ([], [-1,0,1], [2,2,1], [9,5,3]):
    ys = sorted(xs)
    assert Counter(xs) == Counter(ys)
