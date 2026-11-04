# coding: utf-8
# Bài PM01.03 — Tài liệu có thể thực thi độc lập
from sklearn.model_selection import KFold
cv=KFold(n_splits=3,shuffle=True,random_state=1)
splits=list(cv.split(range(9)))
assert len(splits)==3 and all(set(a).isdisjoint(b) for a,b in splits)
