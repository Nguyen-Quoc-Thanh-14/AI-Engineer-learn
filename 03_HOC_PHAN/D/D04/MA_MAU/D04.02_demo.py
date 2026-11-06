# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from typing import TypeVar
T = TypeVar('T')
def first(items: list[T]) -> T | None:
    return items[0] if items else None
assert first(['a','b'])=='a'
assert first([]) is None
print(first([10,20]))
