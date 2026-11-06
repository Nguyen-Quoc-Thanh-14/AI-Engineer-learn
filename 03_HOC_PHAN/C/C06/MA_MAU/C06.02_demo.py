# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from collections import deque
from itertools import chain
q = deque([1,2]); q.appendleft(0)
print(list(q))
print(list(chain([1,2], [3])))
