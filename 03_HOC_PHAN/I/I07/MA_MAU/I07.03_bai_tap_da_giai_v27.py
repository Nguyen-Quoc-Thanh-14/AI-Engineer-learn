# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
def manhattan(p,q):return abs(p[0]-q[0])+abs(p[1]-q[1])
# Bước di chuyển 4 hướng, mỗi bước chi phí 1 => Manhattan admissible.
goal=(2,3)
assert manhattan((0,0),goal)==5
assert manhattan((2,3),goal)==0
# Counterexample: h = 2*Manhattan từ (0,0) =10 > shortest path 5.
assert 2*manhattan((0,0),goal)>5
print('PASS I07.03')
