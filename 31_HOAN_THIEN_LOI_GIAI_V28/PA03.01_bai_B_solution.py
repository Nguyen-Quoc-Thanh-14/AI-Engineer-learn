def validate_records(rows):
    accepted=[];rejected=[]
    for i,row in enumerate(rows):
        q=row.get('qty')
        if type(q) is int and q>=0: accepted.append(row)
        else: rejected.append({'line':i+1,'reason':'qty invalid'})
    return {'accepted':accepted,'rejected':rejected,'rejected_count':len(rejected)}
r=validate_records([{'qty':1},{'qty':-1},{'qty':True},{'qty':0}])
assert len(r['accepted'])==2 and r['rejected_count']==2
