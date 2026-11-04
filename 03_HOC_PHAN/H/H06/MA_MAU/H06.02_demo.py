# coding: utf-8
# Bài H06.02 — Tài liệu có thể thực thi độc lập
xs = [1, 3, 5, -2]
assert sum(xs) == sum(reversed(xs))
assert sum(xs + [0]) == sum(xs)
