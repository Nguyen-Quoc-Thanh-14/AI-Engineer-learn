# coding: utf-8
# Bài PE02.03 — Tài liệu có thể thực thi độc lập
def dedup(rows):return {x['id']:x for x in rows}
assert dedup([{'id':1,'x':2},{'id':1,'x':3}])[1]['x']==3
