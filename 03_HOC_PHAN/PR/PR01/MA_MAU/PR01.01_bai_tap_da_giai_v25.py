# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import ctypes

def copy_bytes(payload: bytes, capacity: int) -> bytes:
    if not isinstance(payload, bytes):
        raise TypeError('payload phải là bytes')
    if type(capacity) is not int or capacity < 0:
        raise ValueError('capacity phải là int không âm')
    if len(payload) > capacity:
        raise ValueError('buffer không đủ chứa dữ liệu')
    buf = ctypes.create_string_buffer(capacity if capacity else 1)
    if payload:
        ctypes.memmove(buf, payload, len(payload))
    return buf.raw[:len(payload)]

def check():
    assert copy_bytes(b'abc', 3) == b'abc'
    assert copy_bytes(b'', 0) == b''
    try: copy_bytes(b'over', 1)
    except ValueError: pass
    else: raise AssertionError('phải chặn overflow')
    try: copy_bytes('text', 10)
    except TypeError: pass
    else: raise AssertionError('sai kiểu')

if __name__ == '__main__':
    check()
    print('OK PR01.01')
