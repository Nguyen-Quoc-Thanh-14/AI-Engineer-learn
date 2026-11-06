# coding: utf-8
# Bài PW01.02 — Tài liệu có thể thực thi độc lập
from fastapi import FastAPI
app=FastAPI()
@app.get('/health')
def health():return {'ok':True}
assert health()=={'ok':True}
