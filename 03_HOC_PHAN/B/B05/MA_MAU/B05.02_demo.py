# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def phi_giao_hang(gia_tri, la_thanh_vien):
    if gia_tri < 0:
        raise ValueError("đơn hàng âm")
    if la_thanh_vien and gia_tri >= 100000:
        return 0
    return 15000
print(phi_giao_hang(100000, True))
print(phi_giao_hang(99999, True))
