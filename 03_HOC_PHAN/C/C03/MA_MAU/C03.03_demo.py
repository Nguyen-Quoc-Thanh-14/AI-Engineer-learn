# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import copy
x = [[1], [2]]
y = copy.copy(x)
z = copy.deepcopy(x)
y[0].append(3)
print(x)
print(z)
