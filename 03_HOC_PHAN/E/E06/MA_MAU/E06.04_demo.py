# coding: utf-8
# Bài E06.04 — Tài liệu có thể thực thi độc lập
def price_after_tax(price, rate):
    if price < 0 or rate < 0: raise ValueError()
    return round(price * (1 + rate), 2)
assert price_after_tax(100, .1) == 110.0
assert price_after_tax(0, .1) == 0
