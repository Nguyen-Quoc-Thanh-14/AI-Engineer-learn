# coding: utf-8
# Bài F04.03 — Tài liệu có thể thực thi độc lập
from hashlib import sha256
placeholder='example-not-real-secret'
assert sha256(placeholder.encode()).digest_size==32
