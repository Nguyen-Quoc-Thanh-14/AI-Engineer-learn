# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def parse_config(port, debug):
    if isinstance(port,bool): raise ValueError('port không được bool')
    try: p=int(port)
    except (ValueError,TypeError): raise ValueError('port phải là số nguyên') from None
    if not 1<=p<=65535: raise ValueError('port range')
    if debug not in ('true','false'): raise ValueError('debug chỉ true/false')
    return p, debug=='true'
assert parse_config('8000','false')==(8000,False)
assert parse_config('443','true')==(443,True)
for invalid in ('0','65536'):
    try: parse_config(invalid,'true')
    except ValueError: pass
    else: raise AssertionError
print('PASS F04.02')
