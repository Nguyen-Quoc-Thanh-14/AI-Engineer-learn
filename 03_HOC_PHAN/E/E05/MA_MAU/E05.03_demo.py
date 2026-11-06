# coding: utf-8
# Bài E05.03 — Tài liệu có thể thực thi độc lập
def subtotal(items):
    return sum(item['quantity'] * item['price'] for item in items)
items = [{'quantity':2, 'price':5}, {'quantity':1, 'price':3}]
assert subtotal(items) == 13
