# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tao():
    dem=0
    def tang():
        nonlocal dem
        dem += 1
        return dem
    return tang
f=tao()
assert [f(),f()] == [1,2]
print(f())
