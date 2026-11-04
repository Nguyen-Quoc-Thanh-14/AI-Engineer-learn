# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
nums = [0, 1, 2, 3, 4]
ket_qua = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
assert ket_qua == [0, 4, 16]
print(ket_qua)
