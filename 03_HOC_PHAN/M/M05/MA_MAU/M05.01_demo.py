# coding: utf-8
# Bài M05.01 — Tài liệu có thể thực thi độc lập
from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
row=(1,'An')
assert User(*row).name=='An'
