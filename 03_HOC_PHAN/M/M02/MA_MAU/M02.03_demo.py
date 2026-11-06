# coding: utf-8
# Bài M02.03 — Tài liệu có thể thực thi độc lập
pages=[{'items':[1,2],'next':1},{'items':[3],'next':None}]
items=[]; cursor=0
while cursor is not None:
    page=pages[cursor]
    items.extend(page['items'])
    cursor=page['next']
assert items==[1,2,3]
