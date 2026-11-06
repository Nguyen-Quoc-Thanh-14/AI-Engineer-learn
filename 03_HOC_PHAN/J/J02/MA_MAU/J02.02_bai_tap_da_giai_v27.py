# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def late_binding(): return [lambda: i for i in range(3)]
def fixed_binding(): return [lambda i=i: i for i in range(3)]
assert [f() for f in late_binding()]==[2,2,2]
assert [f() for f in fixed_binding()]==[0,1,2]
def outer():
    cell='a'
    def get(): return cell
    cell='b'
    return get
assert outer()()=='b'
print('PASS J02.02')
