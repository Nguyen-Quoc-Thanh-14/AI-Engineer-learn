# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from typing import overload
@overload
def parse(value: int) -> int: ...
@overload
def parse(value: str) -> int: ...
def parse(value: int | str) -> int:
    if isinstance(value, bool): raise TypeError('bool không thuộc contract')
    if not isinstance(value, (int, str)): raise TypeError('chỉ int hoặc str')
    if isinstance(value, str) and not value.strip(): raise ValueError('chuỗi rỗng')
    return int(value)
assert parse(12)==12
assert parse(' 07 ')==7
try: parse([])
except TypeError: pass
else: raise AssertionError('runtime check phải từ chối')
# Việc kiểm overload với mypy/pyright KHÔNG được xác nhận bởi các assert runtime này.
print('PASS D06.02')
