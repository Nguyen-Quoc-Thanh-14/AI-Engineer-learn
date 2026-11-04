# coding: utf-8
# Bài J04.03 — Tài liệu có thể thực thi độc lập
class A:
    def f(self): return ['A']
class B(A):
    def f(self): return ['B']+super().f()
class C(B): pass
assert C().f()==['B','A']
assert C.__mro__ == (C,B,A,object)
