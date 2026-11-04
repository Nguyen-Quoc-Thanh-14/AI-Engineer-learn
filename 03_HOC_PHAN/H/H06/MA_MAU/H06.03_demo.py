# coding: utf-8
# Bài H06.03 — Tài liệu có thể thực thi độc lập
def is_adult(age): return age >= 18
assert is_adult(17) is False
assert is_adult(18) is True
assert is_adult(19) is True
