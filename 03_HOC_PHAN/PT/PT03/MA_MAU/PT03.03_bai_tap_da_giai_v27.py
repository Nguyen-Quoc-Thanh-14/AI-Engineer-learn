# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import math
def stable_softmax(xs):
    if not xs:raise ValueError('empty')
    m=max(xs);es=[math.exp(x-m) for x in xs];s=sum(es)
    return [x/s for x in es]
z=stable_softmax([1000,1001,1002])
assert abs(sum(z)-1)<1e-12
assert z[0]<z[1]<z[2]
try:stable_softmax([])
except ValueError:pass
else:raise AssertionError
print('PASS PT03.03')
