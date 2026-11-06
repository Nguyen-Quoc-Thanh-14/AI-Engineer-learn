# Linux-specific: compile tiny shared native library and call via ctypes.
from pathlib import Path
from tempfile import TemporaryDirectory
import ctypes,subprocess,sys
source='double add(double a,double b) { return a+b; }\n'
with TemporaryDirectory() as td:
    root=Path(td);src=root/'ops.c';so=root/'ops.so';src.write_text(source)
    proc=subprocess.run(['gcc','-shared','-fPIC',str(src),'-o',str(so)],capture_output=True,text=True,timeout=10)
    assert proc.returncode==0,proc.stderr
    lib=ctypes.CDLL(str(so));lib.add.argtypes=[ctypes.c_double,ctypes.c_double];lib.add.restype=ctypes.c_double
    assert lib.add(1.25,2.5)==3.75
# This tests Linux local C library, not CPython extension ABI or Windows loader behavior.
