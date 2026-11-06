# coding: utf-8
# Bài L02.02 — Tài liệu có thể thực thi độc lập
from queue import Queue
q=Queue();q.put('a');q.put('b')
assert q.get_nowait()=='a'
assert q.get_nowait()=='b'
assert q.empty()
