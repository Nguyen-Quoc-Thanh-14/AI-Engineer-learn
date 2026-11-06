# coding: utf-8
# Bài M06.02 — Tài liệu có thể thực thi độc lập
processed={}
def charge(key, amount):
    if key in processed:
        if processed[key]!=amount: raise ValueError('conflict')
        return 'already-done'
    processed[key]=amount; return 'done'
assert charge('k1',100)=='done'
assert charge('k1',100)=='already-done'
