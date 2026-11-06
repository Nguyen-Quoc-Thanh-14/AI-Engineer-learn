# coding: utf-8
# Bài N03.03 — Tài liệu có thể thực thi độc lập
event={'actor':'user-123','action':'delete','resource':'doc-9','outcome':'denied'}
assert set(event)=={'actor','action','resource','outcome'}
assert 'password' not in event
