# coding: utf-8
# Bài H03.03 — Tài liệu có thể thực thi độc lập
from collections import Counter
for xs in ([], [1], [3,1,3], list(range(5, -1, -1))):
    out = sorted(xs)
    assert Counter(xs) == Counter(out)
    assert all(a <= b for a, b in zip(out, out[1:]))
