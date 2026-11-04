import importlib.util,sys
sys.dont_write_bytecode = True  # avoid stale pyc for rapid file rewrites
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as td:
    p=Path(td)/'sample.py'
    p.write_text('VALUE = 1\n',encoding='utf-8')
    spec=importlib.util.spec_from_file_location('sample_v28',p)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    bound=mod.VALUE
    p.write_text('VALUE = 2\n',encoding='utf-8')
    # Explicit re-exec avoids filesystem timestamp cache in the demonstration.
    spec.loader.exec_module(mod)
    assert mod.VALUE==2 and bound==1
    sys.modules.pop(spec.name,None)
