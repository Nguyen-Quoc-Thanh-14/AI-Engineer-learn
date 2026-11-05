# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
class PrettyMixin:
    def pretty(self): return f'{type(self).__name__}({self.name!r})'
class Item(PrettyMixin):
    def __init__(self, name): self.name=name
assert Item('a').pretty() == "Item('a')"
assert Item('').pretty() == "Item('')"
assert Item('b').name == 'b'
print('PASS E04.03')
