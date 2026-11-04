# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from math import sqrt
def cosine(a,b):
    if len(a)!=len(b):raise ValueError('dimension mismatch')
    norm_a=sqrt(sum(x*x for x in a));norm_b=sqrt(sum(x*x for x in b))
    if not norm_a or not norm_b:raise ValueError('zero vector')
    return sum(x*y for x,y in zip(a,b))/(norm_a*norm_b)
assert abs(cosine([1,0],[1,0])-1)<1e-12
assert cosine([1,0],[0,1])==0
try:cosine([0,0],[1,2])
except ValueError:pass
else:raise AssertionError
print('PASS PN01.02')
