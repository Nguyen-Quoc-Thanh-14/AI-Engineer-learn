# coding: utf-8
# Bài M07.04 — Tài liệu có thể thực thi độc lập
seen=set(); total=0
for event in [{'id':'e1','value':2},{'id':'e1','value':2},{'id':'e2','value':3}]:
    if event['id'] in seen: continue
    seen.add(event['id']);total+=event['value']
assert total==5
