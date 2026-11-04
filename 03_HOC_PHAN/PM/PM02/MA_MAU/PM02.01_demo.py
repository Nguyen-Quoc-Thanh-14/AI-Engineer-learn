# coding: utf-8
# Bài PM02.01 — Tài liệu có thể thực thi độc lập
from sklearn.linear_model import LinearRegression
m=LinearRegression().fit([[0],[1],[2]],[1,3,5])
assert abs(m.predict([[3]])[0]-7)<1e-8
