# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
class DSU:
    def __init__(self,n):self.parent=list(range(n));self.size=[1]*n;self.count=n
    def root(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]];x=self.parent[x]
        return x
    def union(self,a,b):
        a,b=self.root(a),self.root(b)
        if a==b:return False
        if self.size[a]<self.size[b]:a,b=b,a
        self.parent[b]=a;self.size[a]+=self.size[b];self.count-=1
        return True
d=DSU(4);assert d.count==4
assert d.union(0,1) and d.union(1,2) and d.count==2
assert not d.union(0,2) and d.count==2
print('PASS I07.02')
