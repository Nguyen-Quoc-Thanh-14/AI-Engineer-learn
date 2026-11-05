# coding: utf-8
# Bài M01.03 — Tài liệu có thể thực thi độc lập
import ssl
ctx = ssl.create_default_context()
assert ctx.check_hostname is True
assert ctx.verify_mode == ssl.CERT_REQUIRED
