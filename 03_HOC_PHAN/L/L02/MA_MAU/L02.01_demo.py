# coding: utf-8
# Bài L02.01 — Tài liệu có thể thực thi độc lập
import threading
lock=threading.Lock(); state={'n':0}
def step():
    for _ in range(100):
        with lock: state['n']+=1
threads=[threading.Thread(target=step) for _ in range(2)]
for t in threads:t.start()
for t in threads:t.join()
assert state['n']==200
