# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def is_adult(age):
    if not isinstance(age,int) or isinstance(age,bool): raise TypeError('int')
    return age>=18
# Mutant: dùng >18; test chính xác tại ranh giới 18 sẽ giết mutant.
def mutant(age): return age>18
assert is_adult(17)==False
assert is_adult(18)==True
assert is_adult(19)==True
assert mutant(18)!=is_adult(18)
print('PASS H05.02')
