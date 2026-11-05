# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
ten='ngoai'
def demo():
    ten='trong'
    return ten
assert demo()=='trong'
assert ten=='ngoai'
print(demo(),ten)
