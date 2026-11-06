# coding: utf-8
# Bài PW04.02 — Tài liệu có thể thực thi độc lập
processed=set()
def consume(eid):
    if eid in processed:return False
    processed.add(eid);return True
assert consume('x') and not consume('x')
