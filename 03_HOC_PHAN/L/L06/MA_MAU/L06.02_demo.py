# coding: utf-8
# Bài L06.02 — Tài liệu có thể thực thi độc lập
import threading
class Counter:
    def __init__(self): self.value=0;self.lock=threading.Lock()
    def inc(self):
        with self.lock: self.value+=1
c=Counter(); threads=[threading.Thread(target=c.inc) for _ in range(50)]
for t in threads:t.start()
for t in threads:t.join()
assert c.value==50
