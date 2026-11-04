# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from math import isclose
def trap_square(n):
    h=1/n
    return h*(sum((i*h)**2 for i in range(1,n))+.5)
exact=1/3
errors=[abs(trap_square(n)-exact) for n in [10,20,40]]
assert errors[1]<errors[0]
assert errors[2]<errors[1]
assert errors[0]/errors[1]>3 # bậc ~2
print('PASS PS04.04')
