# coding: utf-8
# Bài PD05.04 — Tài liệu có thể thực thi độc lập
chunks=[[1,2],[3,4,5]]
sums=[sum(c) for c in chunks]
mean=sum(sums)/sum(map(len,chunks))
assert mean==3
