# coding: utf-8
# Bài E06.01 — Tài liệu có thể thực thi độc lập
class Wallet:
    def __init__(self, amount=0):
        if amount < 0: raise ValueError()
        self._amount = amount
    def withdraw(self, n):
        if n < 0 or n > self._amount: raise ValueError()
        self._amount -= n
    @property
    def balance(self): return self._amount
w = Wallet(10)
w.withdraw(7)
assert w.balance == 3
try: w.withdraw(4)
except ValueError: pass
else: raise AssertionError()
assert w.balance == 3
