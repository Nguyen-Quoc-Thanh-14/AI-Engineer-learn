# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from abc import ABC, abstractmethod
class Reader(ABC):
    @abstractmethod
    def read(self, key: str) -> str: ...
class DictReader(Reader):
    def __init__(self, data: dict[str, str]): self._data = dict(data)
    def read(self, key: str) -> str: return self._data[key]
r=DictReader({'a':'alpha'})
assert r.read('a')=='alpha'
try: r.read('missing')
except KeyError: pass
else: raise AssertionError
try: Reader()
except TypeError: pass
else: raise AssertionError
print('PASS E04.02')
