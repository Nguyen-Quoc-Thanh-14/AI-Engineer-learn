# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def upper_bound_speedup(fraction,parallel_accel):
    if not 0<=fraction<=1 or parallel_accel<=0:raise ValueError
    return 1/((1-fraction)+fraction/parallel_accel)
assert abs(upper_bound_speedup(.8,4)-2.5)<1e-10
assert upper_bound_speedup(0,100)==1
assert upper_bound_speedup(.5,2)<2
print('PASS PR03.01')
