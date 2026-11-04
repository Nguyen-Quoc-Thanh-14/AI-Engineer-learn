# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def is_adult(age):
    if not isinstance(age,int) or isinstance(age,bool):raise TypeError()
    if age<0: raise ValueError()
    return age>=18
assert not is_adult(17)
assert is_adult(18)
assert is_adult(19)
