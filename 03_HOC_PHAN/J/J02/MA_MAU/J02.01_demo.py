# coding: utf-8
# Bài J02.01 — Tài liệu có thể thực thi độc lập
def add_item(x, items=None):
    if items is None: items=[]
    items.append(x)
    return items
assert add_item(1)==[1]
assert add_item(2)==[2]
