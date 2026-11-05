import inspect, sys, importlib
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as d:
    p=Path(d)/'entry.py';p.write_text('def api(x, *, default=0): return x+default\n',encoding='utf-8')
    import importlib.util
    spec=importlib.util.spec_from_file_location('entry_test',p)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    assert str(inspect.signature(mod.api))=='(x, *, default=0)'
    assert mod.api(2,default=3)==5
    print('current runtime',sys.version_info[:3])
# Repeat in isolated Python 3.14 and Python 3.15 environments; this local run does NOT establish cross-version compatibility.
