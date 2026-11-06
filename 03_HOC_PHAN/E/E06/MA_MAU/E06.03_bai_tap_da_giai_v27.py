# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def legacy_fetch(key):
    return {'x':10,'y':20}.get(key)
class LegacyAdapter:
    def get(self,key): return legacy_fetch(key)
a=LegacyAdapter()
assert a.get('x')==10
assert a.get('y')==20
assert a.get('missing') is None
print('PASS E06.03')
