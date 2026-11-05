# coding: utf-8
# Bài H04.01 — Tài liệu có thể thực thi độc lập
def divide(a, b):
    if b == 0: raise ZeroDivisionError('denominator is zero')
    return a/b
assert divide(6, 3) == 2
try: divide(1,0)
except ZeroDivisionError as exc: assert 'denominator' in str(exc)
else: raise AssertionError()
