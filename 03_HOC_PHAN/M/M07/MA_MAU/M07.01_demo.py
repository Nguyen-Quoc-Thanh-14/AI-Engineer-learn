# coding: utf-8
# Bài M07.01 — Tài liệu có thể thực thi độc lập
def normalize(payload):
    return {'id':payload['id'],'name':payload.get('name','')}
assert normalize({'id':1})=={'id':1,'name':''}
