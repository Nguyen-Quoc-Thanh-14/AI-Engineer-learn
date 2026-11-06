# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b)
print(a is c)
c[0] = 9
print(a)
