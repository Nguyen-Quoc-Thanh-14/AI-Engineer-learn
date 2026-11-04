# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import ctypes
LIMIT_MIN=-(2**31);LIMIT_MAX=2**31-1
def to_int32(value):
    if type(value) is not int or not LIMIT_MIN<=value<=LIMIT_MAX: raise OverflowError('int32 range')
    return ctypes.c_int32(value).value
assert to_int32(LIMIT_MIN)==LIMIT_MIN
assert to_int32(LIMIT_MAX)==LIMIT_MAX
for bad in (2**31,-(2**31)-1):
    try:to_int32(bad)
    except OverflowError:pass
    else:raise AssertionError
# Không dùng ctypes.c_int32(value) trực tiếp để kiểm miền: ctypes có thể truncate.
print('PASS PR01.03')
