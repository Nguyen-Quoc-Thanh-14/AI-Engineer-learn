# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tim(ds,x):
    lo,hi=0,len(ds)
    while lo<hi:
        mid=(lo+hi)//2
        if ds[mid]<x:lo=mid+1
        else:hi=mid
    return lo if lo<len(ds) and ds[lo]==x else -1
assert tim([1,3,5,7],5)==2
assert tim([1,3,5,7],4)==-1
