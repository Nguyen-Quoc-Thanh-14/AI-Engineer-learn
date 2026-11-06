# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
a = [1, 2]
b = a
b.append(3)
print(a)
print(a is b)
b = [9]
print(a, b)
