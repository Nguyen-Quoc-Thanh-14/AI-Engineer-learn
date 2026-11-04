# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import heapq
h=[]
for x in [4,1,3]: heapq.heappush(h,x)
assert [heapq.heappop(h) for _ in range(3)] == [1,3,4]
