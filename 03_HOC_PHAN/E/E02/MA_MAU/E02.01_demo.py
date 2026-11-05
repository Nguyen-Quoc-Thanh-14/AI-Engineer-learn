# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class Vi:
    def __init__(self,so_du):
        if so_du<0: raise ValueError('âm')
        self._so_du=so_du
    def nap(self,so_tien):
        if so_tien<=0: raise ValueError('phải dương')
        self._so_du+=so_tien
    @property
    def so_du(self): return self._so_du
x=Vi(10);x.nap(5)
assert x.so_du==15
