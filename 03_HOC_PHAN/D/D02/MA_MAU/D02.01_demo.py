# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def ghi_nhan(ham):
    def wrapper(*args, **kwargs):
        kq = ham(*args, **kwargs)
        return {'ket_qua': kq}
    return wrapper

@ghi_nhan
def cong(a, b):
    return a + b

assert cong(2, 5) == {'ket_qua': 7}
print(cong(2, 5))
