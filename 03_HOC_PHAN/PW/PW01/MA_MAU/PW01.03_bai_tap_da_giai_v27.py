# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel,Field
class Input(BaseModel):price:float=Field(gt=0)
app=FastAPI()
@app.post('/products')
def new_product(data:Input):return {'price':data.price}
client=TestClient(app)
assert client.post('/products',json={'price':12}).status_code==200
assert client.post('/products',json={'price':0}).status_code==422
assert client.post('/products',json={'price':-1}).status_code==422
print('PASS PW01.03')
