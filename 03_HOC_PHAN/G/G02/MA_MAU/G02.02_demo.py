# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from io import TextIOWrapper,BytesIO
b=BytesIO('xin chào\n'.encode('utf-8'))
f=TextIOWrapper(b,encoding='utf-8')
assert f.readline()=='xin chào\n'
print('ok')
