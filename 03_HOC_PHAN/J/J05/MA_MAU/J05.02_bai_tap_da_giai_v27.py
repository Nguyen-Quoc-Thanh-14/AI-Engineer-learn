# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
class Service:
    def list(self):return [1,2]
    def count(self):return 2
    def admin_delete(self):return 'danger'
def invoke(s,name):
    allowed={'list':s.list,'count':s.count}
    if name not in allowed:raise ValueError('command not allowed')
    return allowed[name]()
s=Service()
assert invoke(s,'count')==2
assert invoke(s,'list')==[1,2]
for n in ('admin_delete','__class__'):
    try: invoke(s,n)
    except ValueError: pass
    else: raise AssertionError
print('PASS J05.02')
