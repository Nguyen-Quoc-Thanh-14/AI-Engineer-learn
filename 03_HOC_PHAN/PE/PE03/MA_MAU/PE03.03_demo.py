# coding: utf-8
# Bài PE03.03 — Tài liệu có thể thực thi độc lập
def check(rows):
    ids=[r['id'] for r in rows]
    return len(ids)==len(set(ids))
assert check([{'id':1},{'id':2}])
