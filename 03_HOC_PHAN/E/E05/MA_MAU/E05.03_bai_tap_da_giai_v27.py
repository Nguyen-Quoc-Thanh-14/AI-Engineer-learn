# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from dataclasses import dataclass
@dataclass
class Basket:
    prices: list[int]
    def total(self, discount_percent:int=0) -> int:
        if not 0 <= discount_percent <= 100: raise ValueError('discount 0..100')
        return sum(self.prices)*(100-discount_percent)//100
def basket_total(prices, discount_percent=0): return Basket(list(prices)).total(discount_percent)
assert Basket([100,200]).total()==300
assert Basket([100,200]).total(10)==270
assert basket_total([],25)==0
print('PASS E05.03')
