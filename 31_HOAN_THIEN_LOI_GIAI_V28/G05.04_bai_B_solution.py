from pathlib import Path
from tempfile import TemporaryDirectory
import os
# Defensive demonstration; a real adversarial filesystem needs race-safe openat/dirfd mechanisms.
def safe_target(base, name):
    p=(base/name).resolve(strict=False);base=base.resolve()
    if not p.is_relative_to(base): raise ValueError('path traversal/symlink')
    if p.suffix!='.txt': raise ValueError('not a txt file')
    return p
with TemporaryDirectory() as tmp:
    root=Path(tmp);base=root/'uploads';base.mkdir()
    assert safe_target(base,'ok.txt')==base/'ok.txt'
    for name in ('../outside.txt','x/../../bad.txt','file.exe'):
        try: safe_target(base,name)
        except ValueError: pass
        else: raise AssertionError(name)
    outside=root/'outside.txt';outside.write_text('secret',encoding='utf-8')
    symlink=base/'link.txt'
    try: symlink.symlink_to(outside)
    except (OSError,NotImplementedError): pass
    else:
        try: safe_target(base,'link.txt')
        except ValueError: pass
        else: raise AssertionError('symlink escape allowed')
