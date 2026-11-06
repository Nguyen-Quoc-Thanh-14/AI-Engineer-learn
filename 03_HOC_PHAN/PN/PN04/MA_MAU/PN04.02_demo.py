# coding: utf-8
# Bài PN04.02 — Tài liệu có thể thực thi độc lập
claims=[{'text':'x','source_id':'doc-1'}]
known={'doc-1'}
assert all(c['source_id'] in known for c in claims)
