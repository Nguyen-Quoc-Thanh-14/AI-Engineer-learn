# coding: utf-8
# Bài I04.01 — Tài liệu có thể thực thi độc lập
class Key:
    def __init__(self, n): self.n=n
    def __hash__(self): return 1
    def __eq__(self, other): return isinstance(other, Key) and self.n == other.n
x = {Key('a'): 2, Key('b'): 3}
assert x[Key('a')] == 2 and len(x) == 2
