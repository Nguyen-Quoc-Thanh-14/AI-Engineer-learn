# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from copy import deepcopy
original=[{'tags':['a']}]
shallow=original[:];deep=deepcopy(original)
original[0]['tags'].append('b')
assert shallow[0]['tags']==['a','b']
assert deep[0]['tags']==['a']
assert original is not shallow and original[0] is shallow[0]
print('PASS J02.03')
