# coding: utf-8
# Bài PM05.02 — Tài liệu có thể thực thi độc lập
from sklearn.metrics import precision_recall_fscore_support
p,r,f,_=precision_recall_fscore_support([0,0,1,1],[0,0,0,1],average='binary',zero_division=0)
assert p==1 and r==.5
