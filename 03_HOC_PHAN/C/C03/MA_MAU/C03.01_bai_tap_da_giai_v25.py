# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
def append_copy(items: list, value):
    if not isinstance(items, list):
        raise TypeError('items phải là list')
    return [*items, value]

def check():
    original = [1, 2]
    alias = original
    alias.append(3)
    assert original == [1, 2, 3] and alias is original
    result = append_copy(original, 4)
    assert result == [1, 2, 3, 4] and original == [1, 2, 3]
    assert append_copy([], 'x') == ['x']
    try: append_copy(None, 1)
    except TypeError: pass
    else: raise AssertionError('sai kiểu')
    nested = [{'x': 1}]
    copied = append_copy(nested, 2)
    assert copied[0] is nested[0]  # shallow copy

if __name__ == '__main__':
    check()
    print('OK C03.01')
