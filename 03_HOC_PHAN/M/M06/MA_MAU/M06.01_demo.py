# coding: utf-8
# Bài M06.01 — Tài liệu có thể thực thi độc lập
def validate(payload):
    if set(payload)!={'id','qty'}: raise ValueError('keys')
    if type(payload['id']) is not int or type(payload['qty']) is not int: raise TypeError()
    if payload['qty']<0: raise ValueError('negative')
    return payload
assert validate({'id':1,'qty':2})['qty']==2
