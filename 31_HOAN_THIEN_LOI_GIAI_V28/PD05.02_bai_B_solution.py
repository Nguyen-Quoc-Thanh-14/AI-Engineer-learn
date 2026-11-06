import pandas as pd
s=pd.Series([3,pd.NA,1],dtype='Int64')
assert s.isna().sum()==1
mask=s>1
assert str(mask.dtype)=='boolean'
assert s[mask].tolist()==[3]
assert s.sort_values(na_position='last').isna().iloc[-1]
# This checks pandas 2.x behavior only; re-run on pandas 3.x before claiming compatibility.
