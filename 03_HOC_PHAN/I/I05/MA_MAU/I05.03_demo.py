# coding: utf-8
# Bài I05.03 — Tài liệu có thể thực thi độc lập
import heapq
g = {'A':[('B',2),('C',5)],'B':[('C',1)],'C':[]}
d={'A':0}; pq=[(0,'A')]
while pq:
    dist,u=heapq.heappop(pq)
    if dist != d[u]: continue
    for v,w in g[u]:
        nd=dist+w
        if nd<d.get(v,float('inf')): d[v]=nd;heapq.heappush(pq,(nd,v))
assert d['C']==3
