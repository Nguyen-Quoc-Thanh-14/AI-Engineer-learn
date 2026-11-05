# coding: utf-8
# Bài I03.01 — Tài liệu có thể thực thi độc lập
from collections import deque
stack = []
stack.append('a'); stack.append('b')
assert stack.pop() == 'b'
queue = deque(['a','b']); queue.append('c')
assert queue.popleft() == 'a'
