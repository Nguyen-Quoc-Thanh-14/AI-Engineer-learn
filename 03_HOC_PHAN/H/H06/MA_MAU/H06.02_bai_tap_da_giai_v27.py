# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def normalize_space(s): return ' '.join(s.split())
for s in (' A  B ','','á \t b\n', '\u00a0 x  '):
    assert normalize_space(normalize_space(s))==normalize_space(s)
    assert not normalize_space(s).startswith(' ')
assert ' '.join('a  b'.split()) != 'a  b'.strip()
print('PASS H06.02')
