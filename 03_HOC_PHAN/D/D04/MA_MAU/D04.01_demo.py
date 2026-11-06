# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def cong_mot(x: int) -> int:
    return x + 1

assert cong_mot(2)==3
assert cong_mot.__annotations__['x'] is int
print(cong_mot(2))
