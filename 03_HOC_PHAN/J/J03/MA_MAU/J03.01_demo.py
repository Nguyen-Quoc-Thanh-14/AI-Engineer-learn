# coding: utf-8
# Bài J03.01 — Tài liệu có thể thực thi độc lập
xs=iter([10,20])
assert next(xs)==10 and next(xs)==20
try: next(xs)
except StopIteration: pass
else: raise AssertionError()
