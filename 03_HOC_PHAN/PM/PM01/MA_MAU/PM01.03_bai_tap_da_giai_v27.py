# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold,cross_val_score
X,y=make_classification(n_samples=90,n_features=4,n_informative=3,n_redundant=0,random_state=1)
cv=StratifiedKFold(n_splits=3,shuffle=True,random_state=2)
proper=cross_val_score(make_pipeline(StandardScaler(),LogisticRegression(max_iter=500)),X,y,cv=cv)
# Sai về methodology: fit scaler trên TOÀN bộ dữ liệu trước cross-validation (có leakage).
X_leaked=StandardScaler().fit_transform(X)
wrong=cross_val_score(LogisticRegression(max_iter=500),X_leaked,y,cv=cv)
assert len(proper)==3 and len(wrong)==3
assert 0<=proper.mean()<=1
assert 0<=wrong.mean()<=1
# Chênh lệch score không tự chứng minh có/không leakage; chính quy trình fit là bằng chứng.
print('PASS PM01.03')
