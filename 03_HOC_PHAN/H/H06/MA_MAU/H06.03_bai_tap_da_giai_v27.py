# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def can_enter(age): return age>=18
def mutant(age): return age>18
cases={17:False,18:True,19:True}
assert all(can_enter(k)==v for k,v in cases.items())
killed=[k for k,v in cases.items() if mutant(k)!=v]
assert killed==[18]
assert can_enter(18) and not mutant(18)
print('PASS H06.03')
