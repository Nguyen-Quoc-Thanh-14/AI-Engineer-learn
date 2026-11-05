# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def chia(a,b):
    try:
        kq=a/b
    except ZeroDivisionError:
        return None
    else:
        return kq
assert chia(6,2)==3
assert chia(1,0) is None
