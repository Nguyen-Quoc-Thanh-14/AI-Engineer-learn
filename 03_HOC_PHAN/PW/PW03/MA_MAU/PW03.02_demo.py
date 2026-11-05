# coding: utf-8
# Bài PW03.02 — Tài liệu có thể thực thi độc lập
def endpoint(data):
    if 'id' not in data:raise ValueError('missing id')
    return data['id']
assert endpoint({'id':2})==2
