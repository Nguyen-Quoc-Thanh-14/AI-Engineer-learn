# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
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
