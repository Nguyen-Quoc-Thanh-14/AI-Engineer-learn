# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tong(xs):
    total = 0
    for x in xs:
        total += x
    return total
assert tong([])==0
assert tong([2,3,5])==10
print(tong([2,3,5]))
