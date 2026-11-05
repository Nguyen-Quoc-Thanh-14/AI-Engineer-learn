# coding: utf-8
# Bài I03.03 — Tài liệu có thể thực thi độc lập
from collections import deque
from sys import getsizeof
xs = list(range(20))
dq = deque(xs)
assert list(dq) == xs
assert getsizeof(xs) > 0 and getsizeof(dq) > 0
