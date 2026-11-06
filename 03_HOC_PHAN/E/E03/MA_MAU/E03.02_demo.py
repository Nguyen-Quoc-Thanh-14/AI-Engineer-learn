# coding: utf-8
# Bài E03.02 — Tài liệu có thể thực thi độc lập
class NonNegative:
    def __set_name__(self, owner, name): self.name = '_' + name
    def __get__(self, obj, owner=None):
        if obj is None: return self
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value < 0: raise ValueError('negative')
        setattr(obj, self.name, value)
class Account:
    balance = NonNegative()
    def __init__(self, amount): self.balance = amount
x = Account(5)
assert x.balance == 5
try: x.balance = -1
except ValueError: pass
else: raise AssertionError()
