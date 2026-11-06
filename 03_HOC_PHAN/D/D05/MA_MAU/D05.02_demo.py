# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def ty_le(tu: float, mau: float) -> float:
    if mau == 0: raise ValueError('mẫu phải khác 0')
    return tu / mau
assert ty_le(4,2)==2.0
try:ty_le(1,0)
except ValueError: pass
else: raise AssertionError('thiếu tiền điều kiện')
print(ty_le(9,3))
