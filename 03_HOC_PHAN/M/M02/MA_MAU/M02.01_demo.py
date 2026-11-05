# coding: utf-8
# Bài M02.01 — Tài liệu có thể thực thi độc lập
from urllib.parse import urlencode, urlsplit
url = 'https://example.test/api?' + urlencode({'q':'a b'})
assert urlsplit(url).query == 'q=a+b'
