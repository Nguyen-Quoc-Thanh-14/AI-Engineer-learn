import json,pickle
# Threat model: attacker controls upload bytes; pickle can invoke arbitrary code at load time.
def parse_untrusted(blob: bytes):
    if len(blob)>4096: raise ValueError('payload too large')
    obj=json.loads(blob)
    if not isinstance(obj,dict) or set(obj)!={'quantity'}: raise ValueError('bad schema')
    qty=obj['quantity']
    if type(qty) is not int or not 0<=qty<=1000: raise ValueError('bad quantity')
    return qty
assert parse_untrusted(b'{"quantity": 12}')==12
for b in (b'{"quantity": -1}',b'{"quantity": true}',b'[]'):
    try: parse_untrusted(b)
    except ValueError: pass
    else: raise AssertionError('untrusted schema accepted')
# NEVER call pickle.loads on untrusted input.
