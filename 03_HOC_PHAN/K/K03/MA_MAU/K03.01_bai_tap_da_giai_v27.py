# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from itertools import islice
# Không tạo danh sách trung gian: generator lọc số chia hết cho 3.
def stream_total(n):return sum(x for x in range(n) if x%3==0)
assert stream_total(0)==0
assert stream_total(4)==3
assert stream_total(1_000_000)==sum(range(0,1_000_000,3))
print('PASS K03.01')
