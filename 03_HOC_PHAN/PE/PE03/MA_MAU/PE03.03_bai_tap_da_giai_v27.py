# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def validate_batch(rows,expected_count):
    ids=[r.get('id') for r in rows]
    nulls=sum(i is None for i in ids)
    return {'count_ok':len(rows)==expected_count,'unique':len(set(ids))==len(ids),'null_ids':nulls}
a=validate_batch([{'id':1},{'id':2}],2)
assert a=={'count_ok':True,'unique':True,'null_ids':0}
assert not validate_batch([{'id':1},{'id':1}],2)['unique']
assert validate_batch([{'id':None}],1)['null_ids']==1
print('PASS PE03.03')
