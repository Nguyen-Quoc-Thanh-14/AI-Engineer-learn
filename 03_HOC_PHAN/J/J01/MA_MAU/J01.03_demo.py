# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import gc
x=[]
x.append(x)
assert x[0] is x
del x
collected=gc.collect()
assert isinstance(collected,int)
print('GC đã chạy')
