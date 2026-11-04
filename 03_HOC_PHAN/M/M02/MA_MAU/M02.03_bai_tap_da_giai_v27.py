# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def fetch_pages(fetch,max_pages=10):
    cursor=None;seen=set();out=[]
    for _ in range(max_pages):
        rows,next_cursor=fetch(cursor)
        out.extend(rows)
        if next_cursor is None:return out
        if next_cursor in seen:raise ValueError('cursor repeated')
        seen.add(next_cursor);cursor=next_cursor
    raise TimeoutError('page limit')
pages={None:([1,2],'c1'),'c1':([3],None)}
assert fetch_pages(lambda c:pages[c])==[1,2,3]
assert fetch_pages(lambda c:([],None))==[]
try:fetch_pages(lambda c:([1],'same'))
except ValueError:pass
else:raise AssertionError
print('PASS M02.03')
