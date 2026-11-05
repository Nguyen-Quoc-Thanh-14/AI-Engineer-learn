#!/usr/bin/env python3
"""Feature invariants for CPython 3.15.2. Blocks all other versions."""
import sys, platform, json
if sys.implementation.name!='cpython' or sys.version_info[:3] != (3,15,2):
    print('BLOCKED: CPython 3.15.2 is required')
    raise SystemExit(2)
results={}

def check(name,fn):
    try:
        fn();results[name]='PASS'
    except Exception as e:
        results[name]=f'FAIL: {type(e).__name__}: {e}'

def verify_frozendict():
    immutable=frozendict({'env':'prod','retry':3})
    assert hash(immutable)==hash(frozendict({'retry':3,'env':'prod'}))
    assert immutable['retry']==3
    try:
        immutable['retry']=4
    except TypeError:
        return
    raise AssertionError('frozendict unexpectedly mutable')

def verify_sentinel():
    missing=sentinel('MISSING_AUDIT')
    rows={'x':None}
    assert rows.get('x',missing) is None
    assert rows.get('y',missing) is missing

def verify_unpacking():
    xs=eval('[*x for x in [[1, 2], [3], []]]')
    assert xs==[1,2,3]
    d=eval("{**x for x in [{'a':1},{'a':2,'b':3}]}")
    assert d=={'a':2,'b':3}

def verify_lazy_import():
    d={}
    exec('lazy import decimal\nresult=decimal.Decimal("0.1")+decimal.Decimal("0.2")',d)
    assert str(d['result'])=='0.3'

for key,fn in [('frozendict',verify_frozendict),('sentinel',verify_sentinel),
               ('comprehension_unpacked',verify_unpacking),('lazy_import',verify_lazy_import)]:
    check(key,fn)
print(json.dumps({'interpreter':sys.version,'features':results},ensure_ascii=False,indent=2))
raise SystemExit(0 if all(x=='PASS' for x in results.values()) else 1)
