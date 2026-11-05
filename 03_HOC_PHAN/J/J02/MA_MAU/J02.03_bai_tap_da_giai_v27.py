# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from copy import deepcopy
original=[{'tags':['a']}]
shallow=original[:];deep=deepcopy(original)
original[0]['tags'].append('b')
assert shallow[0]['tags']==['a','b']
assert deep[0]['tags']==['a']
assert original is not shallow and original[0] is shallow[0]
print('PASS J02.03')
