# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import unicodedata
text='Python PYTHON'
normalized=unicodedata.normalize('NFC',text).casefold()
assert normalized=='python python'
assert normalized.split()==['python','python']
print(normalized)
