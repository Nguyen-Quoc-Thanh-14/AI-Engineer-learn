# coding: utf-8
# Bài PD03.03 — Tài liệu có thể thực thi độc lập
import pandas as pd
idx=pd.date_range('2026-01-01',periods=4,freq='h',tz='UTC')
s=pd.Series([1,2,3,4],index=idx)
assert s.resample('2h').sum().iloc[0]==3
