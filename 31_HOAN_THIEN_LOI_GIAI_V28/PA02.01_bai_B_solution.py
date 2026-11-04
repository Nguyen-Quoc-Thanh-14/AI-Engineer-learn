def fetch_all(fetch_page,max_pages=10):
    cursor=None;seen=set();result=[]
    for _ in range(max_pages):
        page=fetch_page(cursor)
        result.extend(page['items'])
        cursor=page.get('next')
        if cursor is None:return result
        if cursor in seen:raise ValueError('pagination cycle')
        seen.add(cursor)
    raise RuntimeError('exceeded page limit')
P={None:{'items':[1],'next':'a'},'a':{'items':[2],'next':None}}
assert fetch_all(lambda x:P[x])==[1,2]
try:fetch_all(lambda x:{'items':[],'next':'loop'})
except ValueError:pass
else:raise AssertionError('cycle accepted')
