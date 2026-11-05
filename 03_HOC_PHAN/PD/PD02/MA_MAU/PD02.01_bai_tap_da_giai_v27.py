# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import pandas as pd
x=pd.Series([1,2],index=['a','b']);y=pd.Series([10,20],index=['b','c'])
z=x+y
assert list(z.index)==['a','b','c']
assert z['b']==12
assert pd.isna(z['a']) and pd.isna(z['c'])
print('PASS PD02.01')
