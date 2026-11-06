# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
def append_item(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

def check():
    first = append_item(1)
    second = append_item(2)
    assert first == [1] and second == [2] and first is not second
    provided = []
    assert append_item('x', provided) is provided
    assert provided == ['x']
    provided_empty = []
    append_item(0, provided_empty)
    assert provided_empty == [0]

if __name__ == '__main__':
    check()
    print('OK J02.01')
