# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def fact(n):
    if n < 0:
        raise ValueError("n âm")
    if n == 0:
        return 1
    return n * fact(n - 1)
print(fact(4))
