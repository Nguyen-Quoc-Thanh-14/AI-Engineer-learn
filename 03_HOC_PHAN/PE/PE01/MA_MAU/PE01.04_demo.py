# coding: utf-8
# Bài PE01.04 — Tài liệu có thể thực thi độc lập
rows=[{'id':1,'ts':4},{'id':2,'ts':6}]
watermark=5
assert [r['id'] for r in rows if r['ts']>watermark]==[2]
