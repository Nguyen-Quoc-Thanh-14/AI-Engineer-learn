# coding: utf-8
# Bài I05.02 — Tài liệu có thể thực thi độc lập
from collections import deque
g = {'A':['B','C'],'B':['D'],'C':[],'D':[]}
q=deque(['A']); seen={'A'}; order=[]
while q:
    node=q.popleft(); order.append(node)
    for nxt in g[node]:
        if nxt not in seen: seen.add(nxt);q.append(nxt)
assert order == ['A','B','C','D']
