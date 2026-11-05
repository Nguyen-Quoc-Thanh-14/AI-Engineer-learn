# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
class Denied(PermissionError):pass
def access(user_id,role,owner_id,operation):
    if operation not in {'read','write'}:raise ValueError
    if role!='admin' and user_id!=owner_id:raise Denied
    return True
cases=[(1,'user',1,'read',True),(1,'user',1,'write',True),
       (2,'user',1,'read',False),(2,'user',1,'write',False),
       (2,'admin',1,'read',True),(2,'admin',1,'write',True)]
for uid,role,owner,op,expected in cases:
    try:got=access(uid,role,owner,op)
    except Denied:got=False
    assert got is expected
print('PASS N04.02')
