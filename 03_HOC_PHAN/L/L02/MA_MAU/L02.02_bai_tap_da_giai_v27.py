# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from queue import Queue
from threading import Thread
Q=Queue(maxsize=3);STOP=object();out=[]
def consumer():
    while True:
        item=Q.get(timeout=2)
        try:
            if item is STOP:return
            out.append(item*2)
        finally:Q.task_done()
t=Thread(target=consumer);t.start()
for value in [1,2,3]:Q.put(value,timeout=2)
Q.put(STOP,timeout=2);Q.join();t.join(timeout=2)
assert not t.is_alive() and out==[2,4,6]
print('PASS L02.02')
