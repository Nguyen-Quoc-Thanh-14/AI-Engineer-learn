# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tao_bo_dem():
    dem = 0
    def tang():
        nonlocal dem
        dem += 1
        return dem
    return tang

a, b = tao_bo_dem(), tao_bo_dem()
assert [a(), a(), b(), a()] == [1, 2, 1, 3]
print(a(), b())
