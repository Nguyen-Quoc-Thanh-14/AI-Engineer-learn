# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from io import StringIO
with StringIO('dòng 1\n') as f:
    assert f.readline()=='dòng 1\n'
print('đóng')
