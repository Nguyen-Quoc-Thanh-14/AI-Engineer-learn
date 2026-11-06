# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import os,tempfile
from pathlib import Path
from tempfile import TemporaryDirectory
def atomic_write_text(path: Path, text: str):
    tmp=None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,delete=False) as f:
            tmp=Path(f.name);f.write(text);f.flush();os.fsync(f.fileno())
        os.replace(tmp,path)
    finally:
        if tmp is not None and tmp.exists(): tmp.unlink()
with TemporaryDirectory() as t:
    p=Path(t)/'record.txt'
    atomic_write_text(p,'á');assert p.read_text(encoding='utf-8')=='á'
    atomic_write_text(p,'b');assert p.read_text()=='b'
    assert len(list(Path(t).iterdir()))==1
print('PASS G04.02')
