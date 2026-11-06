# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def lower_bound(xs,target):
    lo,hi=0,len(xs)
    while lo<hi:
        mid=(lo+hi)//2
        if xs[mid]<target: lo=mid+1
        else: hi=mid
    return lo
assert lower_bound([1,2,2,2,4],2)==1
assert lower_bound([],10)==0
assert lower_bound([1,2,2,4],3)==3
# Invariant: mọi index <lo có giá trị < target, mọi index >=hi có giá trị >=target.
print('PASS I06.01')
