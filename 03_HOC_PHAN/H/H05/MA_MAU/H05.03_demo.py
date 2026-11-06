# coding: utf-8
# Bài H05.03 — Tài liệu có thể thực thi độc lập
def calc_old(prices):
    total = 0
    for p in prices: total += p
    return total

def calc_new(prices): return sum(prices)
for data in ([], [1,2], [-2, 3]): assert calc_old(data) == calc_new(data)
