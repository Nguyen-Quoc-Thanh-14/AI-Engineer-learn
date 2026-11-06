# coding: utf-8
# Bài PD05.01 — Tài liệu có thể thực thi độc lập
import pandas as pd
df=pd.DataFrame({'x':[1,2]})
df.loc[df['x']==1,'x']=5
assert df['x'].tolist()==[5,2]
