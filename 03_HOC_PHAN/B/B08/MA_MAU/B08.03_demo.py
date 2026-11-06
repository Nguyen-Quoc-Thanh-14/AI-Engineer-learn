# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tong_vong_lap(n):
    total = 0
    for x in range(n + 1):
        total += x
    return total
print(tong_vong_lap(10))
