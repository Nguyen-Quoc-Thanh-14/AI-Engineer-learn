# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def binh_phuong(n):
    for x in range(n):
        yield x*x
g = binh_phuong(4)
print(next(g))
print(list(g))
