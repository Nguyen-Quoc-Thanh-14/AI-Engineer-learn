# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
a=[]
b=a
assert b is a
del a
b.append(1)
assert b==[1]
print('Đối tượng vẫn tồn tại:',b)
