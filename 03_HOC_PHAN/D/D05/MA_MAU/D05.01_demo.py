# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def gia_sau_giam(gia: float, *, ty_le: float=0.1) -> float:
    if not 0 <= ty_le <= 1: raise ValueError('ty_le phải từ 0 đến 1')
    return gia * (1 - ty_le)
assert gia_sau_giam(100, ty_le=0.2)==80.0
print(gia_sau_giam(100))
