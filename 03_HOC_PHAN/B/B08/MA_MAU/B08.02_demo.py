# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def dem_xuong(n):
    print("vao", n)
    if n == 0:
        return
    dem_xuong(n - 1)
    print("ra", n)
dem_xuong(2)
