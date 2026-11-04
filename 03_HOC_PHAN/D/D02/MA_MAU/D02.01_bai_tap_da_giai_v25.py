# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from functools import wraps

def nonnegative(func):
    @wraps(func)
    def wrapper(value):
        if type(value) not in (int, float):
            raise TypeError('cần số')
        if value < 0:
            raise ValueError('không âm')
        return func(value)
    return wrapper

@nonnegative
def square(value):
    """Bình phương số không âm."""
    return value * value

def check():
    assert square(3) == 9
    assert square(0) == 0
    assert square.__name__ == 'square'
    try: square(-1)
    except ValueError: pass
    else: raise AssertionError('chưa validate')
    try: square('3')
    except TypeError: pass
    else: raise AssertionError('chưa validate kiểu')

if __name__ == '__main__':
    check()
    print('OK D02.01', square(3))
