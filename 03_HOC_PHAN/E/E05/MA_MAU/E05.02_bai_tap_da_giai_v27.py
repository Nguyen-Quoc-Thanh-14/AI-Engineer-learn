# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from dataclasses import dataclass
@dataclass(frozen=True)
class Money:
    amount: int  # đơn vị nhỏ nhất; không dùng float cho tiền
    currency: str
    def __post_init__(self):
        if isinstance(self.amount,bool) or not isinstance(self.amount,int): raise TypeError('amount phải là int')
        if len(self.currency)!=3 or not self.currency.isalpha(): raise ValueError('ISO-like code 3 chữ')
a=Money(1500,'VND'); b=Money(1500,'VND')
assert a==b and hash(a)==hash(b)
assert len({a,b,Money(100,'USD')})==2
try: Money(1.5,'USD')
except TypeError: pass
else: raise AssertionError
print('PASS E05.02')
