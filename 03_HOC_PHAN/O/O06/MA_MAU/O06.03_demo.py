# coding: utf-8
# Bài O06.03 — Tài liệu có thể thực thi độc lập
from hashlib import sha256
artifact=b'build-output'
release_sha=sha256(artifact).hexdigest()
assert len(release_sha)==64
