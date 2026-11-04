# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
ds=[('A',2),('B',1),('C',2)]
r=sorted(ds,key=lambda x:x[1])
assert r==[('B',1),('A',2),('C',2)]
print(r)
