# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
class PrettyMixin:
    def pretty(self): return f'{type(self).__name__}({self.name!r})'
class Item(PrettyMixin):
    def __init__(self, name): self.name=name
assert Item('a').pretty() == "Item('a')"
assert Item('').pretty() == "Item('')"
assert Item('b').name == 'b'
print('PASS E04.03')
