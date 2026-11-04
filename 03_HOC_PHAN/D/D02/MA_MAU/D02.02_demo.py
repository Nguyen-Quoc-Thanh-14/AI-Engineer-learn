# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from functools import wraps

def nhan_he_so(he_so):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return he_so * fn(*args, **kwargs)
        return wrapper
    return decorator

@nhan_he_so(3)
def cong(a, b):
    """Cộng hai số."""
    return a + b

assert cong(2, 4) == 18
assert cong.__name__ == 'cong'
assert cong.__wrapped__(2, 4) == 6
print(cong.__doc__)
