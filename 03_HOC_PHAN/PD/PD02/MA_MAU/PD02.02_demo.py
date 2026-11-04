# coding: utf-8
# Bài PD02.02 — Tài liệu có thể thực thi độc lập
import pandas as pd
left=pd.DataFrame({'id':[1,2],'qty':[2,3]});right=pd.DataFrame({'id':[1,2],'price':[4,5]})
x=left.merge(right,on='id',validate='one_to_one')
assert x.eval('qty*price').sum()==23
