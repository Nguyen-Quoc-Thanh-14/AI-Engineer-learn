# coding: utf-8
# Bài I07.03 — Tài liệu có thể thực thi độc lập
from collections import deque
g={'A':['B','C'],'B':['D'],'C':['D'],'D':[]}
q=deque(['A']);seen={'A'}
while q:
    x=q.popleft()
    for y in g[x]:
        if y not in seen: seen.add(y);q.append(y)
assert seen==set(g)
