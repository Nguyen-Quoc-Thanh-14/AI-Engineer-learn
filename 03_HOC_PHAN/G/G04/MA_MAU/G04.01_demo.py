# coding: utf-8
# Bài G04.01 — Tài liệu có thể thực thi độc lập
from io import BytesIO
stream = BytesIO(b'abcde')
chunks = []
while True:
    block = stream.read(2)
    if not block: break
    chunks.append(block)
assert chunks == [b'ab', b'cd', b'e']
