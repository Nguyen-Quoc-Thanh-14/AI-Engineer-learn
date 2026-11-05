# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class Gio:
    loai='hop'
    def __init__(self,ten): self.ten=ten
    def xem(self): return self.ten
x=Gio('A'); y=Gio('B')
assert (x.xem(),y.xem(),Gio.loai)==('A','B','hop')
