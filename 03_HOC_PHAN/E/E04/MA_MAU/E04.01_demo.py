# coding: utf-8
# Bài E04.01 — Tài liệu có thể thực thi độc lập
class Base:
    def who(self): return ['Base']
class Left(Base):
    def who(self): return ['Left'] + super().who()
class Right(Base):
    def who(self): return ['Right'] + super().who()
class Child(Left, Right): pass
assert Child().who() == ['Left', 'Right', 'Base']
assert Child.__mro__[1:3] == (Left, Right)
