# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from functools import lru_cache
CONFIG={'rate':2}
@lru_cache(maxsize=16)
def compute(key):return key*CONFIG['rate']
assert compute(3)==6
CONFIG['rate']=5
assert compute(3)==6  # cache cũ còn hiệu lực
compute.cache_clear()
assert compute(3)==15
print('PASS K03.02')
