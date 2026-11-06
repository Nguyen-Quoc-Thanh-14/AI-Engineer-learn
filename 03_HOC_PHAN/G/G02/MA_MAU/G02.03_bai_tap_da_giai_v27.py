# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
import struct
HEADER=struct.Struct('!HI')  # phiên bản 2 bytes, độ dài 4 bytes; big endian
def encode(payload: bytes, version=1) -> bytes:
    if len(payload) > 1024: raise ValueError('too long')
    return HEADER.pack(version,len(payload))+payload
def decode(blob: bytes):
    if len(blob)<HEADER.size: raise ValueError('truncated header')
    version,length=HEADER.unpack(blob[:HEADER.size])
    if length>1024 or len(blob)!=HEADER.size+length: raise ValueError('invalid length')
    return version,blob[HEADER.size:]
assert decode(encode(b'abc'))==(1,b'abc')
assert decode(encode(b''))==(1,b'')
try: decode(b'123')
except ValueError: pass
else: raise AssertionError
print('PASS G02.03')
