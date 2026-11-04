# Backfill with merge keyed on partition and business record ID, preserving newer periods.
store={('2026-10',1):{'quantity':2},('2026-11',2):{'quantity':4}}
def ingest(month,orders):
    for order in orders:
        key=(month,order['id'])
        store[key]={'quantity':order['quantity']}
ingest('2026-10',[{'id':1,'quantity':3}])
assert store[('2026-10',1)]['quantity']==3
assert store[('2026-11',2)]['quantity']==4
before=dict(store);ingest('2026-10',[{'id':1,'quantity':3}]);assert store==before
