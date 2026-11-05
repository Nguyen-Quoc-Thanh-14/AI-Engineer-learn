# coding: utf-8
# Bài I04.03 — Tài liệu có thể thực thi độc lập
import heapq
h = []
for priority, value in [(3,'c'),(1,'a'),(2,'b')]: heapq.heappush(h,(priority,value))
assert [heapq.heappop(h)[1] for _ in range(3)] == ['a','b','c']
