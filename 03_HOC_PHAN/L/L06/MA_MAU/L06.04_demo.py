# coding: utf-8
# Bài L06.04 — Tài liệu có thể thực thi độc lập
import threading
from queue import Queue
q=Queue()
threads=[threading.Thread(target=lambda i=i:q.put(i)) for i in range(20)]
for t in threads:t.start()
for t in threads:t.join()
assert q.qsize()==20
