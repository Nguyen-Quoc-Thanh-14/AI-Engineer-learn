# coding: utf-8
# Bài PM01.02 — Tài liệu có thể thực thi độc lập
from sklearn.model_selection import train_test_split
x=list(range(100))
a,b=train_test_split(x,test_size=.2,random_state=42)
assert len(a)==80 and len(b)==20 and set(a).isdisjoint(b)
