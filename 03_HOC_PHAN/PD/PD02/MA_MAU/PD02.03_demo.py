# coding: utf-8
# Bài PD02.03 — Tài liệu có thể thực thi độc lập
import pandas as pd
s=pd.Series([1,None],dtype='Int64')
assert pd.isna(s.iloc[1])
assert s.notna().sum()==1
