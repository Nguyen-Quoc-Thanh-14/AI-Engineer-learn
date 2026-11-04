# coding: utf-8
# Bài E05.02 — Tài liệu có thể thực thi độc lập
from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int
a, b = Point(1, 2), Point(1, 2)
assert a == b and hash(a) == hash(b)
assert {a: 'ok'}[b] == 'ok'
assert 'Point' in repr(a)
