# coding: utf-8
# Bài E06.03 — Tài liệu có thể thực thi độc lập
def total(prices, policy):
    return sum(policy(price) for price in prices)
regular = lambda p: p
sale = lambda p: p * 0.9
assert total([100, 200], regular) == 300
assert total([100, 200], sale) == 270
