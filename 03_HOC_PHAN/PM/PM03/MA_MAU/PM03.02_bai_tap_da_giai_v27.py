# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from statistics import mean,median,stdev
xs=[10,10,11,11,12,1000]
avg=mean(xs);med=median(xs);mad=median(abs(x-med) for x in xs)
assert avg>med*10
assert med==11
assert mad==1
print('PASS PM03.02')
