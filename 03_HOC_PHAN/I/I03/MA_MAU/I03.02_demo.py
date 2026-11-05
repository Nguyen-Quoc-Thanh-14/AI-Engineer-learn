# coding: utf-8
# Bài I03.02 — Tài liệu có thể thực thi độc lập
from dataclasses import dataclass
@dataclass
class Node:
    value: int
    next: object = None
head = Node(1, Node(2))
assert head.value == 1 and head.next.value == 2
