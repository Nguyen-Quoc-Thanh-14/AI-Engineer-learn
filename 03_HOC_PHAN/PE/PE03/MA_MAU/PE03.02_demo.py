# coding: utf-8
# Bài PE03.02 — Tài liệu có thể thực thi độc lập
from pathlib import PurePosixPath
p=PurePosixPath('orders/year=2026/month=11/part-001.parquet')
assert 'year=2026' in p.parts
