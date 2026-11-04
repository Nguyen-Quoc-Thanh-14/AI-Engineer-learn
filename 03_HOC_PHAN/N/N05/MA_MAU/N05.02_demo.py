# coding: utf-8
# Bài N05.02 — Tài liệu có thể thực thi độc lập
import hashlib
blob=b'package'
expected=hashlib.sha256(blob).hexdigest()
assert hashlib.sha256(blob).hexdigest()==expected
