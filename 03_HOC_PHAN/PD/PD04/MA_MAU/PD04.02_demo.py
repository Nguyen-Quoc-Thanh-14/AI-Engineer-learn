# coding: utf-8
# Bài PD04.02 — Tài liệu có thể thực thi độc lập
import pandas as pd
df=pd.DataFrame({'qty':[1,None,-1,3]})
valid=df['qty'].notna() & (df['qty']>=0)
assert valid.sum()==2
