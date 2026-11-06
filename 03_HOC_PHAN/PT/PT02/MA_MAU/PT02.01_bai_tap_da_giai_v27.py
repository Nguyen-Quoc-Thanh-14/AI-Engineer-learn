# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from math import comb
from fractions import Fraction
probabilities={k:Fraction(comb(3,k),8) for k in range(4)}
assert probabilities[0]==Fraction(1,8)
assert probabilities[1]==Fraction(3,8)
assert sum(probabilities.values())==1
print('PASS PT02.01')
