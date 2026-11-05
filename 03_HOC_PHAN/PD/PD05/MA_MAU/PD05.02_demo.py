# coding: utf-8
# Bài PD05.02 — Tài liệu có thể thực thi độc lập
import pandas as pd
s=pd.Series(['An',None],dtype='string')
assert s.isna().sum()==1
