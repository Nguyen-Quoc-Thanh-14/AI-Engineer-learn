# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import math
from random import Random

def estimate_pi(samples: int, seed: int = 0) -> float:
    if type(samples) is not int or samples < 1:
        raise ValueError('samples phải là int dương')
    rng = Random(seed)
    inside = 0
    for _ in range(samples):
        x, y = rng.random(), rng.random()
        inside += (x*x + y*y <= 1)
    return 4*inside/samples

def check():
    assert estimate_pi(10000, seed=7) == estimate_pi(10000, seed=7)
    assert abs(estimate_pi(100000, seed=1) - math.pi) < 0.05
    assert 0 <= estimate_pi(1, seed=0) <= 4
    try: estimate_pi(0)
    except ValueError: pass
    else: raise AssertionError('samples 0')

if __name__ == '__main__':
    check()
    print('OK PS02.01', estimate_pi(10000, 7))
