# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from io import BytesIO
from zipfile import ZipFile
buf=BytesIO()
with ZipFile(buf, 'w') as z:
    z.writestr('a.txt','A');z.writestr('b.txt','B')
buf.seek(0)
with ZipFile(buf) as z:
    assert sorted(z.namelist())==['a.txt','b.txt']
    assert z.read('a.txt')==b'A'
    assert z.read('b.txt')==b'B'
print('PASS G04.03')
