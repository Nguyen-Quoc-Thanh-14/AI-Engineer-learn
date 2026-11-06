# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
class Account:
    def __init__(self, balance=0):
        if isinstance(balance,bool) or not isinstance(balance,int) or balance<0: raise ValueError
        self._balance=balance
    @property
    def balance(self): return self._balance
    def deposit(self, amount:int):
        if isinstance(amount,bool) or not isinstance(amount,int) or amount<=0: raise ValueError
        self._balance+=amount
        return self._balance
a=Account(10)
assert a.deposit(5)==15
try: a.deposit(-5)
except ValueError: pass
else: raise AssertionError
assert a.balance==15
print('PASS E06.01')
