# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from functools import wraps

def khong_rong(fn):
    @wraps(fn)
    def wrapper(text):
        if not text.strip(): raise ValueError('rỗng')
        return fn(text)
    return wrapper

@khong_rong
def viet_hoa(text): return text.strip().title()
assert viet_hoa('  python  ') == 'Python'
print(viet_hoa('  python  '))
