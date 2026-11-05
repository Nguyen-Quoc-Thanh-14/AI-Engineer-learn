# coding: utf-8
# Bài PE01.03 — Tài liệu có thể thực thi độc lập
rows=[{'id':1},{'id':2}]
assert len({r['id'] for r in rows})==len(rows)
