# coding: utf-8
# Bài PD03.01 — Tài liệu có thể thực thi độc lập
import pandas as pd
s=pd.Series([1,2,2,5]);assert s.median()==2
assert s.value_counts().loc[2]==2
