# coding: utf-8
# Bài E03.01 — Tài liệu có thể thực thi độc lập
class Temperature:
    def __init__(self, celsius): self.celsius = celsius
    @property
    def celsius(self): return self._celsius
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)): raise TypeError('number required')
        if value < -273.15: raise ValueError('below absolute zero')
        self._celsius = value
x = Temperature(25)
assert x.celsius == 25
try: x.celsius = -300
except ValueError: pass
else: raise AssertionError('validation missing')
