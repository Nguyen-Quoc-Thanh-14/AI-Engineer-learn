# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import uuid,json
def error_response(code,message,status,request_id=None):
    if status not in {400,409,500}:raise ValueError('unexpected status')
    return status,{'code':code,'message':message,'request_id':request_id or 'r-test'}
for n in [400,409,500]:
    status,payload=error_response('INVALID','bad',n)
    assert status==n and set(payload)=={'code','message','request_id'}
assert json.loads(json.dumps(error_response('x','y',400)[1]))['code']=='x'
print('PASS M06.01')
