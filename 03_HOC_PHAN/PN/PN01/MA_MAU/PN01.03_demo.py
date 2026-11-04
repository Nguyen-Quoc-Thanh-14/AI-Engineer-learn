# coding: utf-8
# Bài PN01.03 — Tài liệu có thể thực thi độc lập
documents=['python typing','python pandas','database query']
retrieved=[x for x in documents if 'python' in x]
assert len(retrieved)==2
