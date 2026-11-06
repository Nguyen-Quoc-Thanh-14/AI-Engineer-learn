# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
class IdempotencyStore:
    def __init__(self):self.saved={}
    def post(self,key,amount):
        if not key or amount<=0: return 400,None
        previous=self.saved.get(key)
        if previous is not None:
            return (200,previous) if previous['amount']==amount else (409,None)
        result={'amount':amount,'payment_id':len(self.saved)+1}
        self.saved[key]=result
        return 201,result
s=IdempotencyStore()
assert s.post('k',100)[0]==201
assert s.post('k',100)[0]==200
assert s.post('k',101)[0]==409
print('PASS M06.02')
