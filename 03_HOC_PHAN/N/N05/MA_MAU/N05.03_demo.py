# coding: utf-8
# Bài N05.03 — Tài liệu có thể thực thi độc lập
import ssl
ctx=ssl.create_default_context()
assert ctx.verify_mode==ssl.CERT_REQUIRED
assert ctx.check_hostname
