# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from pathlib import Path
from tempfile import TemporaryDirectory
from hashlib import sha256
def sha256_file(path, chunk=7):
    if chunk<1: raise ValueError('chunk')
    h=sha256()
    with open(path,'rb') as f:
        for block in iter(lambda:f.read(chunk),b''): h.update(block)
    return h.hexdigest()
with TemporaryDirectory() as t:
    p=Path(t)/'x.bin'
    p.write_bytes(b'');assert sha256_file(p)==sha256(b'').hexdigest()
    p.write_bytes(b'12345678');assert sha256_file(p)==sha256(b'12345678').hexdigest()
    try: sha256_file(p,0)
    except ValueError: pass
    else: raise AssertionError
print('PASS G04.01')
