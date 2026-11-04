# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from timeit import repeat

def squares_loop(n):
    result = []
    for x in range(n):
        result.append(x * x)
    return result

def squares_comprehension(n):
    return [x * x for x in range(n)]

def measure(stmt):
    samples = repeat(stmt, number=100, repeat=3)
    assert len(samples) == 3 and min(samples) >= 0
    return min(samples), samples

def check():
    for n in (0, 1, 100):
        assert squares_loop(n) == squares_comprehension(n)
    baseline, samples = measure(lambda: squares_loop(100))
    assert baseline >= 0 and len(samples) == 3

if __name__ == '__main__':
    check()
    print('OK K01.01 (không kết luận thuật toán nào nhanh hơn nếu chưa đo)')
