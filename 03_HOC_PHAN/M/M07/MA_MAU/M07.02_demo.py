# coding: utf-8
# Bài M07.02 — Tài liệu có thể thực thi độc lập
from urllib.parse import urlsplit
url=urlsplit('https://example.test/resource')
assert url.scheme=='https'
assert url.hostname=='example.test'
