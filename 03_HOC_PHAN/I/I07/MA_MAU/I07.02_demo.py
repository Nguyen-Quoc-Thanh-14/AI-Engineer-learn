# coding: utf-8
# Bài I07.02 — Tài liệu có thể thực thi độc lập
parent=list(range(4))
def find(x):
    if parent[x]!=x: parent[x]=find(parent[x])
    return parent[x]
def union(a,b): parent[find(b)]=find(a)
union(0,1);union(1,2)
assert find(0)==find(2) and find(3)!=find(0)
