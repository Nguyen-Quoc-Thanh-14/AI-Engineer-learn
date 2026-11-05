# coding: utf-8
# Bài H05.02 — Tài liệu có thể thực thi độc lập
def fee(amount): return 0 if amount == 0 else amount * 0.05
assert fee(0) == 0
assert fee(100) == 5
assert fee(20) == 1
