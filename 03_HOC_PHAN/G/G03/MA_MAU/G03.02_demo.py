# coding: utf-8
# Bài G03.02 — Tài liệu có thể thực thi độc lập
import json
obj = json.loads('{"name":"An","age":21}')
assert isinstance(obj['name'], str)
assert type(obj['age']) is int
assert json.loads(json.dumps(obj)) == obj
