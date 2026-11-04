# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from datetime import datetime,timedelta
def merge_incremental(stored,incoming,cutoff):
    result=dict(stored)
    for row in incoming:
        if row['updated_at']>=cutoff:
            id=row['id'];old=result.get(id)
            if old is None or row['updated_at']>=old['updated_at']:result[id]=row
    return result
start=datetime(2026,1,1);cutoff=start+timedelta(days=1)
old={1:{'id':1,'updated_at':start,'v':'old'}}
new=[{'id':1,'updated_at':cutoff,'v':'new'}, {'id':2,'updated_at':start,'v':'too old'}]
result=merge_incremental(old,new,cutoff)
assert result[1]['v']=='new'
assert 2 not in result
assert len(result)==1
print('PASS PE01.04')
