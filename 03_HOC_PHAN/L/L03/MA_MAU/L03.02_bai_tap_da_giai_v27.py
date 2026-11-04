# coding: utf-8
from concurrent.futures import ProcessPoolExecutor

def square(n: int) -> int:
    return n*n

def batch_square(numbers):
    with ProcessPoolExecutor(max_workers=2) as pool:
        return list(pool.map(square, numbers))

if __name__ == '__main__':
    assert batch_square([2, 3, -4]) == [4, 9, 16]
    assert batch_square([0]) == [0]
    assert batch_square([]) == []
    print('PASS L03.02')
