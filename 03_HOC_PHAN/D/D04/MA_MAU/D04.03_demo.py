# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from typing import Protocol
class Writer(Protocol):
    def write(self, text: str) -> None: ...

class Buffer:
    def __init__(self): self.messages=[]
    def write(self, text: str) -> None: self.messages.append(text)

def gui(w: Writer, text: str) -> None: w.write(text)
b = Buffer(); gui(b,'xin chao')
assert b.messages == ['xin chao']
print(b.messages)
