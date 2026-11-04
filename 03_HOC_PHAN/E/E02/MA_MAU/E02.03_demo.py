# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class Sms:
    def gui(self,x):return 'sms:'+x
class Email:
    def gui(self,x):return 'email:'+x
def thong_bao(k,noi_dung):return k.gui(noi_dung)
assert thong_bao(Sms(),'A')=='sms:A'
assert thong_bao(Email(),'A')=='email:A'
