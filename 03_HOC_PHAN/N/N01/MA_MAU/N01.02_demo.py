# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import re
def ma_hop_le(text):
    return isinstance(text,str) and re.fullmatch(r'[A-Z]{2}-[0-9]{4}',text) is not None
assert ma_hop_le('AB-1234')
assert not ma_hop_le('../etc/passwd')
assert not ma_hop_le('AB-1234 extra')
