# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from math import sin,pi
from scipy.integrate import quad
def trap(n):
    h=pi/n
    return h*(sum(sin(i*h) for i in range(1,n))+.5*(sin(0)+sin(pi)))
exact,_=quad(sin,0,pi)
assert abs(exact-2)<1e-10
assert abs(trap(100)-exact)<.001
assert abs(trap(1000)-exact)<abs(trap(100)-exact)
print('PASS PS01.02')
