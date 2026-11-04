# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tinh_thanh_tien(gia,sl):
    if min(gia,sl)<0:raise ValueError()
    return gia*sl
# Arrange
gia,so_luong=100,2
# Act
actual=tinh_thanh_tien(gia,so_luong)
# Assert
assert actual==200
