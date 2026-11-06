# coding: utf-8
# Bài PA04.03 — Tài liệu có thể thực thi độc lập
from collections import deque
events=deque(['x','x','y']);seen=set();out=[]
while events:
    p=events.popleft()
    if p not in seen:seen.add(p);out.append(p)
assert out==['x','y']
