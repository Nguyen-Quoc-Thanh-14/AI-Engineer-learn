# coding: utf-8
# Bài G04.03 — Tài liệu có thể thực thi độc lập
import gzip, io, zipfile
x = b'hello' * 20
assert gzip.decompress(gzip.compress(x)) == x
bio = io.BytesIO()
with zipfile.ZipFile(bio, 'w') as z: z.writestr('a.txt', 'ok')
with zipfile.ZipFile(bio) as z: assert z.read('a.txt') == b'ok'
