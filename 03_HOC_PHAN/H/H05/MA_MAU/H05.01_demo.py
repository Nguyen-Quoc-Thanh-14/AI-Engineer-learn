# coding: utf-8
# Bài H05.01 — Tài liệu có thể thực thi độc lập
def sum_two(a: int, b: int) -> int:
    return a + b
assert sum_two(2, 3) == 5
assert sum_two.__annotations__['return'] is int
