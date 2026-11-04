# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
data = [1,2,3,4]
print([x*x for x in data if x%2 == 0])
print({x: x*x for x in data if x<3})
