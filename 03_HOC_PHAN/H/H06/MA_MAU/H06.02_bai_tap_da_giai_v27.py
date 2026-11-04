# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def normalize_space(s): return ' '.join(s.split())
for s in (' A  B ','','á \t b\n', '\u00a0 x  '):
    assert normalize_space(normalize_space(s))==normalize_space(s)
    assert not normalize_space(s).startswith(' ')
assert ' '.join('a  b'.split()) != 'a  b'.strip()
print('PASS H06.02')
