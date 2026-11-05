# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import pandas as pd
frame=pd.DataFrame({'category':['a','b','a'],'qty':[2,3,4],'price':[10,2,5]})
frame['revenue']=frame['qty']*frame['price']
result=frame.groupby('category')['revenue'].sum().to_dict()
assert result=={'a':40,'b':6}
assert frame['category'].nunique()==2
assert sum(result.values())==frame['revenue'].sum()
print('PASS PD02.02')
