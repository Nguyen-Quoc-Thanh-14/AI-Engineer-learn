# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
class Item(BaseModel):id:int;name:str
app=FastAPI()
@app.get('/items',response_model=list[Item])
def list_items():return [{'id':1,'name':'a'}]
client=TestClient(app)
r=client.get('/items')
assert r.status_code==200
assert r.json()==[{'id':1,'name':'a'}]
assert isinstance(r.json(),list)
print('PASS PW01.02')
