# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
X,y=make_classification(n_samples=120,n_features=5,n_redundant=0,random_state=9)
Xtr,Xte,ytr,yte=train_test_split(X,y,random_state=7,stratify=y)
scores=[m.fit(Xtr,ytr).score(Xte,yte) for m in (DummyClassifier(strategy='most_frequent'),LogisticRegression(max_iter=500))]
assert len(scores)==2
assert all(0<=s<=1 for s in scores)
assert scores[1]>=scores[0]  # chỉ xác minh trên dữ liệu mô phỏng đã cố định seed
print('PASS PM03.03')
