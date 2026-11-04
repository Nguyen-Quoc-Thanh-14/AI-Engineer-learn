# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tinh_gia(gia, so_luong=1, *, thue=0.1):
    return gia * so_luong * (1 + thue)
print(tinh_gia(100))
print(tinh_gia(100, 2, thue=0))
