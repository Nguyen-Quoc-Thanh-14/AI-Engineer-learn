# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import json
MAX=1024*1024
ALLOWED={'id','name'}
def parse_body(raw:bytes):
    if not isinstance(raw,bytes) or len(raw)>MAX:raise ValueError('request size')
    obj=json.loads(raw)
    if not isinstance(obj,dict) or set(obj)-ALLOWED:raise ValueError('keys')
    return obj
assert parse_body(b'{"id":1}')=={'id':1}
for raw in (b'{"admin":true}',b'a'*(MAX+1)):
    try:parse_body(raw)
    except ValueError:pass
    else:raise AssertionError
print('PASS N02.03')
