# coding: utf-8
# Bài G05.03 — Tài liệu có thể thực thi độc lập
import json
raw = '{"id": 3, "qty": 2}'
assert len(raw.encode()) < 1000
x = json.loads(raw)
if set(x) != {'id', 'qty'} or type(x['qty']) is not int or x['qty'] < 0:
    raise ValueError('bad schema')
assert x['qty'] == 2
