# coding: utf-8
# Bài N02.02 — Tài liệu có thể thực thi độc lập
from hashlib import sha256
payload=b'demo artifact'
digest=sha256(payload).hexdigest()
assert len(digest)==64
