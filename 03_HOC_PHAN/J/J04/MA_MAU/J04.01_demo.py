# coding: utf-8
# Bài J04.01 — Tài liệu có thể thực thi độc lập
class A:
    @property
    def score(self): return 5
a=A()
assert a.score==5
assert 'score' not in vars(a)
assert 'score' in vars(A)
