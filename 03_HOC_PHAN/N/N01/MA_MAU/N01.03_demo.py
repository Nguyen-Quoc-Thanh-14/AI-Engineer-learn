# coding: utf-8
# Bài N01.03 — Tài liệu có thể thực thi độc lập
roles={'alice':{'read'},'bob':{'read','write'}}
def allowed(user,action): return action in roles.get(user,set())
assert allowed('alice','read') and not allowed('alice','write')
