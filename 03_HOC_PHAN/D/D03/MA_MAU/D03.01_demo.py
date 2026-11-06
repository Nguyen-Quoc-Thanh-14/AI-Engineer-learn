# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        return x
    return inner
f = outer()
assert f() == 'enclosing'
print(f())
