# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
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
