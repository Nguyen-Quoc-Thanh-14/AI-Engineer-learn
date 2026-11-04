# coding: utf-8
# Bài PM03.01 — Tài liệu có thể thực thi độc lập
from sklearn.decomposition import PCA
X=[[1,0],[2,0],[3,0]]
p=PCA(n_components=1).fit_transform(X)
assert p.shape==(3,1)
