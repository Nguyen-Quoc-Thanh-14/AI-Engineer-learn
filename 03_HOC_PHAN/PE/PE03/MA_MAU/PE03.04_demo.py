# coding: utf-8
# Bài PE03.04 — Tài liệu có thể thực thi độc lập
from itertools import islice
rows=iter(range(1_000))
assert list(islice(rows,3))==[0,1,2]
