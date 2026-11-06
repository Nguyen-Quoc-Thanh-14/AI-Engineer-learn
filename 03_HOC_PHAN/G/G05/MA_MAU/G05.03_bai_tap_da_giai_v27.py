# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import json
def schema_check(raw:bytes):
    if len(raw)>100: raise ValueError('too many bytes')
    obj=json.loads(raw)
    if type(obj) is not dict or set(obj)!={'id','name'}: raise ValueError('invalid keys')
    if type(obj['id']) is not int or type(obj['name']) is not str: raise ValueError('types')
    return obj
assert schema_check(b'{"id":1,"name":"x"}')['id']==1
for payload in [b'{"id":1,"name":"x","admin":true}',b'x'*101]:
    try: schema_check(payload)
    except ValueError: pass
    else: raise AssertionError
print('PASS G05.03')
