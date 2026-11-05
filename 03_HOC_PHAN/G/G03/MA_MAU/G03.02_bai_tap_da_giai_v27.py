# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import json
def validate_user(data):
    if not isinstance(data,dict) or set(data)!={'name','age'}: raise ValueError('schema')
    if not isinstance(data['name'],str) or not data['name'].strip(): raise ValueError('name')
    if type(data['age']) is not int or data['age']<0: raise ValueError('age')
    return {'name':data['name'].strip(),'age':data['age']}
assert validate_user(json.loads('{"name":" A ","age":0}'))=={'name':'A','age':0}
for data in ({'name':'','age':1},{'name':'A','age':True}):
    try: validate_user(data)
    except ValueError: pass
    else: raise AssertionError
print('PASS G03.02')
