# coding: utf-8
# Bài I06.02 — Tài liệu có thể thực thi độc lập
coins=[4,3,1]
remaining=6; greedy=[]
for coin in coins:
    while remaining>=coin: greedy.append(coin);remaining-=coin
assert len(greedy)==3 and greedy==[4,1,1]
assert sum([3,3])==6
