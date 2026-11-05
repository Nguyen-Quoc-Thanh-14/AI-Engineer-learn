# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class NhanTin:
    def send(self,x):return 'send:'+x
class DonHang:
    def __init__(self,notifier):self.notifier=notifier
    def xac_nhan(self):return self.notifier.send('ok')
assert DonHang(NhanTin()).xac_nhan()=='send:ok'
