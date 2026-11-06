# coding: utf-8
# Bài PM03.03 — Tài liệu có thể thực thi độc lập
from sklearn.dummy import DummyClassifier
m=DummyClassifier(strategy='most_frequent').fit([[0],[1],[2]],[0,0,1])
assert m.predict([[9]]).tolist()==[0]
