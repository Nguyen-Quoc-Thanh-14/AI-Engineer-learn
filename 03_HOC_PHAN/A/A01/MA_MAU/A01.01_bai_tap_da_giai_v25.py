# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
def line_total(unit_price: int, quantity: int) -> int:
    """Trả tổng tiền cho số nguyên không âm, không có tác dụng phụ."""
    for value in (unit_price, quantity):
        if type(value) is not int:
            raise TypeError("unit_price và quantity phải là int")
        if value < 0:
            raise ValueError("không được âm")
    return unit_price * quantity


def check():
    assert line_total(12, 3) == 36
    assert line_total(9, 0) == 0
    try:
        line_total(-2, 5)
    except ValueError:
        pass
    else:
        raise AssertionError("không chặn đầu vào âm")
    try:
        line_total(True, 1)
    except TypeError:
        pass
    else:
        raise AssertionError("bool không thuộc hợp đồng")

if __name__ == '__main__':
    check()
    print('OK A01.01', line_total(12, 3))
