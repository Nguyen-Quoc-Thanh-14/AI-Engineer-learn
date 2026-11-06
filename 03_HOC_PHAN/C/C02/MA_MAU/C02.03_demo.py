# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
d = {(1, 2): "điểm"}
print(d[(1, 2)])
try:
    d[[1, 2]] = "sai"
except TypeError:
    print("unhashable")
