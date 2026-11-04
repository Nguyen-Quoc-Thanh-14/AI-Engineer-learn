# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import importlib
import math
import sys

def square_root(x):
    if type(x) not in (int, float):
        raise TypeError('cần số')
    if x < 0:
        raise ValueError('căn thực không xác định cho số âm')
    module = importlib.import_module('math')
    return module.sqrt(x)

def check():
    assert square_root(9) == 3.0
    assert square_root(0) == 0.0
    assert importlib.import_module('math') is math
    assert sys.modules['math'] is math
    try: square_root(-1)
    except ValueError: pass
    else: raise AssertionError('miền âm')
    try: importlib.import_module('not_a_real_module_93486')
    except ModuleNotFoundError: pass
    else: raise AssertionError('module không tồn tại')

if __name__ == '__main__':
    check()
    print('OK F01.01', square_root(9))
