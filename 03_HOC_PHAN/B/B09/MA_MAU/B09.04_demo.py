# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from decimal import Decimal, ROUND_HALF_UP
x = Decimal("2.345")
print(x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
print(int(-2.9))
