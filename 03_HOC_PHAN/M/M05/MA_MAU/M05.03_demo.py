# coding: utf-8
# Bài M05.03 — Tài liệu có thể thực thi độc lập
users=[{'id':1},{'id':2},{'id':3}]
orders={1:[10],2:[],3:[20,30]}
# Một phép batch lookup từ map giả lập thay vì một lần I/O per user.
result=[(u['id'],orders.get(u['id'],[])) for u in users]
assert sum(len(x[1]) for x in result)==3
