# coding: utf-8
# Bài PM02.03 — Tài liệu có thể thực thi độc lập
from sklearn.metrics import brier_score_loss
score=brier_score_loss([0,1],[.1,.9])
assert abs(score-.01)<1e-12
