# coding: utf-8
# Bài PM04.01 — Tài liệu có thể thực thi độc lập
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
m=make_pipeline(StandardScaler(),LogisticRegression()).fit([[0],[1],[2],[3]],[0,0,1,1])
assert m.predict([[2.5]])[0]==1
