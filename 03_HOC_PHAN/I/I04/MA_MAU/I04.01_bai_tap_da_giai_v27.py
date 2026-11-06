# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
class Key:
    def __init__(self,n): self.n=n
    def __hash__(self): return 1  # chủ đích tạo collision
    def __eq__(self,other): return isinstance(other,Key) and self.n==other.n
items={Key(i): i*10 for i in range(100)}
assert len(items)==100
assert items[Key(27)]==270
assert Key(100) not in items
# Đúng về mặt key equality, nhưng 100 collisions có thể làm suy giảm hiệu suất.
print('PASS I04.01')
