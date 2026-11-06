# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
X=np.array([['red',1.0],['blue',np.nan],['red',3.0]],dtype=object)
pre=ColumnTransformer([
 ('category',OneHotEncoder(handle_unknown='ignore'),[0]),
 ('number',SimpleImputer(strategy='median'),[1])])
Z=pre.fit_transform(X)
assert Z.shape==(3,3)
assert np.isfinite(Z.astype(float)).all()
assert pre.transform(np.array([['other',np.nan]],dtype=object)).shape==(1,3)
print('PASS PM04.01')
