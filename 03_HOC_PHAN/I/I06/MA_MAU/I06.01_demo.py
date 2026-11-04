# coding: utf-8
# Bài I06.01 — Tài liệu có thể thực thi độc lập
def binary_search(xs, target):
    lo,hi=0,len(xs)
    while lo < hi:
        mid=(lo+hi)//2
        if xs[mid]<target: lo=mid+1
        else: hi=mid
    return lo if lo<len(xs) and xs[lo]==target else -1
assert binary_search([1,3,7],3)==1
assert binary_search([],5)==-1
