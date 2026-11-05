# coding: utf-8
# Bài E04.03 — Tài liệu có thể thực thi độc lập
class ToDictMixin:
    def to_dict(self): return dict(vars(self))
class User(ToDictMixin):
    def __init__(self, name): self.name = name
assert User('Linh').to_dict() == {'name': 'Linh'}
