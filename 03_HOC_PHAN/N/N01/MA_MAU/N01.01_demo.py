# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def limit_name(x):
    if not isinstance(x,str) or not 1<=len(x)<=20:
        raise ValueError('Tên không hợp lệ')
    return x
assert limit_name('An')=='An'
try:limit_name('')
except ValueError:pass
else:raise AssertionError()
