# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from fastapi import FastAPI
from fastapi.testclient import TestClient
app=FastAPI()
@app.get('/v1/users/1')
def v1():return {'name':'A'}
@app.get('/v2/users/1')
def v2():return {'name':'A','display_name':'A'}
c=TestClient(app)
assert c.get('/v1/users/1').json()=={'name':'A'}
assert c.get('/v2/users/1').json()['display_name']=='A'
assert c.get('/v3/users/1').status_code==404
print('PASS PW03.01')
