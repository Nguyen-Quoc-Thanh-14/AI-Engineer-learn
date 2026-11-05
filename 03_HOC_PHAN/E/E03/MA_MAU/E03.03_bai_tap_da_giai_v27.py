# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def normalize_name(text: str) -> str:
    if not isinstance(text, str): raise TypeError('chỉ nhận str')
    return ' '.join(text.split()).title()
assert normalize_name('  nguyen   van   a ') == 'Nguyen Van A'
assert normalize_name('') == ''
try: normalize_name(None)
except TypeError: pass
else: raise AssertionError
print('PASS E03.03')
