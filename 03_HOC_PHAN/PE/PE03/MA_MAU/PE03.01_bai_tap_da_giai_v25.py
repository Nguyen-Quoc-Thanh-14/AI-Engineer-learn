# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import hashlib
from pathlib import Path
from tempfile import TemporaryDirectory

def snapshot_digest(folder: Path) -> str:
    folder = Path(folder)
    if not folder.is_dir():
        raise NotADirectoryError(folder)
    digest = hashlib.sha256()
    for path in sorted(p for p in folder.rglob('*') if p.is_file()):
        rel = path.relative_to(folder).as_posix().encode('utf-8')
        digest.update(len(rel).to_bytes(8, 'big'))
        digest.update(rel)
        content = path.read_bytes()
        digest.update(len(content).to_bytes(8, 'big'))
        digest.update(content)
    return digest.hexdigest()

def check():
    with TemporaryDirectory() as tmp:
        folder = Path(tmp)
        path = folder/'data.txt'
        path.write_bytes(b'abc')
        old = snapshot_digest(folder)
        assert snapshot_digest(folder) == old
        path.write_bytes(b'abd')
        assert snapshot_digest(folder) != old
        assert len(snapshot_digest(folder)) == 64
    try: snapshot_digest('/path/definitely/not/exists/99712')
    except NotADirectoryError: pass
    else: raise AssertionError('directory missing')

if __name__ == '__main__':
    check()
    print('OK PE03.01')
