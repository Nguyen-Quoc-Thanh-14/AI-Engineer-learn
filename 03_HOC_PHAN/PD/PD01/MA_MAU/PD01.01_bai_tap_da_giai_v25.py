# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import numpy as np

def shift_columns(matrix, offsets):
    matrix = np.asarray(matrix, dtype=float)
    offsets = np.asarray(offsets, dtype=float)
    if matrix.ndim != 2 or offsets.ndim != 1:
        raise ValueError('matrix 2D, offsets 1D')
    if matrix.shape[1] != offsets.shape[0]:
        raise ValueError('số cột phải bằng số offset')
    return matrix + offsets

def check():
    result = shift_columns([[1, 2], [3, 4]], [10, 20])
    assert np.array_equal(result, [[11, 22], [13, 24]])
    assert shift_columns(np.empty((0, 2)), [1, 2]).shape == (0, 2)
    for a, b in (([1, 2], [10, 20]), ([[1, 2]], [1, 2, 3])):
        try: shift_columns(a, b)
        except ValueError: pass
        else: raise AssertionError('shape sai phải báo lỗi')

if __name__ == '__main__':
    check()
    print('OK PD01.01')
