# coding: utf-8
# Bài PW01.03 — Tài liệu có thể thực thi độc lập
from fastapi import FastAPI
app=FastAPI()
@app.get('/items/{item_id}')
def get_item(item_id:int):return {'item_id':item_id}
assert get_item(7)['item_id']==7
