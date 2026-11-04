# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from typing import TypeVar
T = TypeVar('T')  # tương đương cú pháp generic theo PEP 695, tương thích 3.13+
def first(items: list[T]) -> T:
    if not items: raise ValueError('danh sách không được rỗng')
    return items[0]
assert first([5, 9]) == 5
assert first(['x', 'y']) == 'x'
try: first([])
except ValueError: pass
else: raise AssertionError('phải từ chối rỗng')
print('PASS D06.01')
