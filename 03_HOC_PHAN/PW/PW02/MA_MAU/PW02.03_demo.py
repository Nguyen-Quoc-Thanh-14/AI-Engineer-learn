# coding: utf-8
# Bài PW02.03 — Tài liệu có thể thực thi độc lập
cache={}
def get_or_set(k,fn):
    if k not in cache:cache[k]=fn()
    return cache[k]
assert get_or_set('a',lambda:2)==2
