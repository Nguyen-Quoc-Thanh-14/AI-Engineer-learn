# coding: utf-8
# Bài PM02.02 — Tài liệu có thể thực thi độc lập
from sklearn.tree import DecisionTreeClassifier
m=DecisionTreeClassifier(max_depth=2,random_state=0).fit([[0],[1],[2]],[0,0,1])
assert m.predict([[2]]).tolist()==[1]
