# coding: utf-8
# Bài G02.03 — Tài liệu có thể thực thi độc lập
import struct
encoded = struct.pack('>HI', 7, 500)
assert len(encoded) == 6
assert struct.unpack('>HI', encoded) == (7, 500)
