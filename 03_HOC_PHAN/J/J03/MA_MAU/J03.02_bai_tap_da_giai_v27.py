# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def records(prefix,n):
    for i in range(n): yield f'{prefix}:{i}'
def all_records():
    yield from records('a',2)
    yield from records('b',1)
assert list(all_records())==['a:0','a:1','b:0']
assert list(records('none',0))==[]
assert next(iter(records('x',1)))=='x:0'
print('PASS J03.02')
