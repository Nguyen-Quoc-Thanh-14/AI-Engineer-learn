import pandas as pd
from sklearn.impute import SimpleImputer
s=pd.Series([1,pd.NA,3],dtype='Int64')
assert s.isna().sum()==1
arr=SimpleImputer(strategy='median').fit_transform(s.to_frame())
assert arr.shape==(3,1) and float(arr[1,0])==2.
