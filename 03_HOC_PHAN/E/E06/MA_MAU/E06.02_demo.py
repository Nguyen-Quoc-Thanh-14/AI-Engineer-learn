# coding: utf-8
# Bài E06.02 — Tài liệu có thể thực thi độc lập
class InMemoryRepo:
    def __init__(self): self.data = {'x': 7}
    def get(self, key): return self.data[key]
class Service:
    def __init__(self, repo): self.repo = repo
    def double(self, key): return 2 * self.repo.get(key)
assert Service(InMemoryRepo()).double('x') == 14
