def time_splits(records,train_until,val_until):
    train=[r for r in records if r['date']<train_until]
    val=[r for r in records if train_until<=r['date']<val_until]
    test=[r for r in records if r['date']>=val_until]
    return train,val,test
rows=[{'date':i,'target':i%2} for i in range(12)]
a,b,c=time_splits(rows,6,9)
assert len(a)==6 and len(b)==3 and len(c)==3
assert max(x['date'] for x in a)<min(x['date'] for x in b)
# Target encoding statistics must be estimated within training folds only.
