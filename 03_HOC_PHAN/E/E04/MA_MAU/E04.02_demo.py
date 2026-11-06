# coding: utf-8
# Bài E04.02 — Tài liệu có thể thực thi độc lập
from abc import ABC, abstractmethod
class Storage(ABC):
    @abstractmethod
    def get(self, key): ...
class Memory(Storage):
    def __init__(self): self.data = {'a': 3}
    def get(self, key): return self.data[key]
assert Memory().get('a') == 3
try: Storage()
except TypeError: pass
else: raise AssertionError()
