# coding: utf-8
# Bài PM03.02 — Tài liệu có thể thực thi độc lập
from statistics import mean,pstdev
xs=[1,2,2,3,100]; mu=mean(xs);sigma=pstdev(xs)
assert (100-mu)/sigma>1
