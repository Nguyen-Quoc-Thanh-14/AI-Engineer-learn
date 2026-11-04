# coding: utf-8
# Bài K03.03 — Tài liệu có thể thực thi độc lập
def batches(xs,n):
    for i in range(0,len(xs),n): yield xs[i:i+n]
assert list(batches([1,2,3,4,5],2))==[[1,2],[3,4],[5]]
