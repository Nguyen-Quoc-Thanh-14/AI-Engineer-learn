# coding: utf-8
# Bài G05.02 — Tài liệu có thể thực thi độc lập
import unicodedata
s1 = 'é'
s2 = 'é'
assert s1 != s2
assert unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2)
