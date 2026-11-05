# coding: utf-8
# Bài E05.01 — Tài liệu có thể thực thi độc lập
from dataclasses import dataclass, field
from enum import Enum
class Status(Enum): OPEN = 'open'; CLOSED = 'closed'
@dataclass
class Task:
    title: str
    status: Status = Status.OPEN
    labels: list[str] = field(default_factory=list)
a, b = Task('A'), Task('B')
a.labels.append('urgent')
assert b.labels == [] and a.status is Status.OPEN
