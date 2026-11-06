# coding: utf-8
# Bài G05.01 — Tài liệu có thể thực thi độc lập
s = 'Tiếng Việt'
b = s.encode('utf-8')
assert b.decode('utf-8') == s
assert len(b) > len(s)
