from tempfile import TemporaryDirectory
from pathlib import Path
import subprocess, sys
with TemporaryDirectory() as tmp:
    p=Path(tmp)
    (p/'a.py').write_text('from b import b_func\ndef a_func(): return "A"\n',encoding='utf-8')
    (p/'b.py').write_text('from a import a_func\ndef b_func(): return "B"\n',encoding='utf-8')
    bad=subprocess.run([sys.executable,'-I','-c','import sys;sys.path.insert(0,sys.argv[1]);import a',str(p)],capture_output=True,text=True,timeout=5)
    assert bad.returncode!=0 and 'ImportError' in bad.stderr
    (p/'common.py').write_text('def shared(): return "OK"\n',encoding='utf-8')
    (p/'a.py').write_text('from common import shared\ndef a_func(): return shared()+"A"\n',encoding='utf-8')
    (p/'b.py').write_text('from common import shared\ndef b_func(): return shared()+"B"\n',encoding='utf-8')
    ok=subprocess.run([sys.executable,'-I','-c','import sys;sys.path.insert(0,sys.argv[1]);import a,b;assert a.a_func()=="OKA" and b.b_func()=="OKB"',str(p)],capture_output=True,text=True,timeout=5)
    assert ok.returncode==0,ok.stderr
