# coding: utf-8
# Bài H03.01 — Tài liệu có thể thực thi độc lập
def palindrome(s): return s == s[::-1]
cases = [('', True), ('aa', True), ('ab', False)]
for value, expected in cases:
    assert palindrome(value) is expected
