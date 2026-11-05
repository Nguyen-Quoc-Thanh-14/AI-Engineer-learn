# coding: utf-8
# Bài N02.03 — Tài liệu có thể thực thi độc lập
import json
raw='{"count":2}'
if len(raw)>100: raise ValueError()
data=json.loads(raw)
assert set(data)=={'count'} and type(data['count']) is int
