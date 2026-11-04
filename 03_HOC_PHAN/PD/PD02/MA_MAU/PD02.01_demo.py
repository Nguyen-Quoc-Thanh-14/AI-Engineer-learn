# coding: utf-8
# Bài PD02.01 — Tài liệu có thể thực thi độc lập
import pandas as pd
a=pd.Series([1,2],index=['x','y']);b=pd.Series([3],index=['x'])
assert (a+b).loc['x']==4
assert pd.isna((a+b).loc['y'])
