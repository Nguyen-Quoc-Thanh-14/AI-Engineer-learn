# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

def money_sum(*values: str) -> Decimal:
    """Cộng chuỗi thập phân hợp lệ và làm tròn 0.01, HALF_UP."""
    total = Decimal('0')
    for value in values:
        if not isinstance(value, str):
            raise TypeError('giá trị phải là chuỗi thập phân')
        try:
            amount = Decimal(value)
        except InvalidOperation as exc:
            raise ValueError('giá trị không phải số') from exc
        if not amount.is_finite():
            raise ValueError('không nhận NaN/Infinity')
        total += amount
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def check():
    assert money_sum('0.1', '0.2') == Decimal('0.30')
    assert money_sum() == Decimal('0.00')
    assert money_sum('1.005') == Decimal('1.01')
    for invalid in ('NaN', 'not-a-number'):
        try: money_sum(invalid)
        except ValueError: pass
        else: raise AssertionError('phải từ chối dữ liệu lỗi')

if __name__ == '__main__':
    check()
    print('OK B09.01', money_sum('0.1', '0.2'))
