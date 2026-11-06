# coding: utf-8
# Bài PE01.02 — Tài liệu có thể thực thi độc lập
def transform(rows):return [{'id':r['id'],'qty':int(r['qty'])} for r in rows]
assert transform([{'id':1,'qty':'3'}])[0]['qty']==3
