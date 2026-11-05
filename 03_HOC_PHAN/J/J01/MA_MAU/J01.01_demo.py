# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
a=[1,2]
b=a
c=a.copy()
assert a is b
assert a is not c
assert a==c
b.append(3)
assert a==[1,2,3] and c==[1,2]
print(a,c)
