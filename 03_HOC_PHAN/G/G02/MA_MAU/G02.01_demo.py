# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
text='Tiếng Việt'
raw=text.encode('utf-8')
assert raw.decode('utf-8')==text
assert len(raw)>len(text)
print(len(text),len(raw))
