# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import math

def central_difference(f, x: float, step: float = 1e-5) -> float:
    if not (step > 0 and math.isfinite(step)):
        raise ValueError('step phải dương và hữu hạn')
    return (f(x+step)-f(x-step))/(2*step)

def check():
    for x in (-2.0, 0.0, 3.0):
        assert math.isclose(central_difference(lambda v: v*v, x), 2*x, abs_tol=1e-9)
    try: central_difference(lambda x: x*x, 1.0, 0)
    except ValueError: pass
    else: raise AssertionError('step 0')
    assert math.isclose(central_difference(lambda x: (x+2)**2, 1), 6.0, abs_tol=1e-9)

if __name__ == '__main__':
    check()
    print('OK PT03.01')
