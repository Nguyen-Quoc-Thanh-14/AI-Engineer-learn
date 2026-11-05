# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from threading import Lock,Thread
from contextlib import contextmanager
lock1,lock2=Lock(),Lock();hits=[]
@contextmanager
def ordered_locks():
    with lock1:
        with lock2:yield
def update(i):
    with ordered_locks():hits.append(i)
threads=[Thread(target=update,args=(i,)) for i in range(10)]
for t in threads:t.start()
for t in threads:t.join(timeout=2)
assert len(hits)==10
assert all(not t.is_alive() for t in threads)
print('PASS L02.03')
