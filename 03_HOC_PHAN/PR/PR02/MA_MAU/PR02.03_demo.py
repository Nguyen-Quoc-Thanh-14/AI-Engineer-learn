# coding: utf-8
# Bài PR02.03 — Tài liệu có thể thực thi độc lập
try:
    int('x')
except ValueError as e:
    assert isinstance(e,ValueError)
else:raise AssertionError()
