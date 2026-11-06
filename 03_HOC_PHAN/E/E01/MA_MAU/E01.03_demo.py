# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class X:
    def __init__(self): self.ready=True
x=X()
assert x.ready
print(x.__dict__)
