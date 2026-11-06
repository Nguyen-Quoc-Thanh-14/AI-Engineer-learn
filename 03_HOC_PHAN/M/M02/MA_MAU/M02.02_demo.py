# coding: utf-8
# Bài M02.02 — Tài liệu có thể thực thi độc lập
def delays(base, attempts):
    return [min(8, base * 2 ** i) for i in range(attempts)]
assert delays(1, 5) == [1,2,4,8,8]
