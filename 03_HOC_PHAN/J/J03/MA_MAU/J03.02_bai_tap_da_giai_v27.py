# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def records(prefix,n):
    for i in range(n): yield f'{prefix}:{i}'
def all_records():
    yield from records('a',2)
    yield from records('b',1)
assert list(all_records())==['a:0','a:1','b:0']
assert list(records('none',0))==[]
assert next(iter(records('x',1)))=='x:0'
print('PASS J03.02')
