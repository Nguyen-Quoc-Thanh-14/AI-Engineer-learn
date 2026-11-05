# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def chuyen(x):
    try:return int(x)
    except ValueError:return None
assert chuyen('42')==42
assert chuyen('x') is None
print(chuyen('x'))
