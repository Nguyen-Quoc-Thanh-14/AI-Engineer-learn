# coding: utf-8
# Bài PM05.01 — Tài liệu có thể thực thi độc lập
from sklearn.model_selection import GroupShuffleSplit
ids=list(range(6)); groups=['a','a','b','b','c','c']
a,b=next(GroupShuffleSplit(test_size=1/3,random_state=1).split(ids,groups=groups))
assert set(groups[i] for i in a).isdisjoint(groups[i] for i in b)
