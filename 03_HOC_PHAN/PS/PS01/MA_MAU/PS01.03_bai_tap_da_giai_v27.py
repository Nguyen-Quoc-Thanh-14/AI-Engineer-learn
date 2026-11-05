# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from math import sin,cos
x=.5
errors=[]
for h in (0.1,0.01,0.001):
    approx=(sin(x+h)-sin(x-h))/(2*h)
    errors.append(abs(approx-cos(x)))
assert errors[1]<errors[0]
assert errors[2]<errors[1]
assert len(errors)==3
print('PASS PS01.03')
