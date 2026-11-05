# coding: utf-8
# Bài PW03.01 — Tài liệu có thể thực thi độc lập
from fastapi import FastAPI
app=FastAPI(title='Demo')
schema=app.openapi()
assert schema['info']['title']=='Demo'
