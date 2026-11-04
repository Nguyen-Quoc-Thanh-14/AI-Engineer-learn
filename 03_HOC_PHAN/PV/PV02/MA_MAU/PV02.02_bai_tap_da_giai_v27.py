# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def iou(a,b):
    ax1,ay1,ax2,ay2=a;bx1,by1,bx2,by2=b
    if ax2<ax1 or ay2<ay1 or bx2<bx1 or by2<by1:raise ValueError
    w=max(0,min(ax2,bx2)-max(ax1,bx1))
    h=max(0,min(ay2,by2)-max(ay1,by1))
    intersection=w*h;area_a=(ax2-ax1)*(ay2-ay1);area_b=(bx2-bx1)*(by2-by1)
    return intersection/(area_a+area_b-intersection) if area_a+area_b-intersection else 0
assert iou((0,0,2,2),(0,0,2,2))==1
assert iou((0,0,1,1),(2,2,3,3))==0
assert abs(iou((0,0,2,2),(1,1,3,3))-1/7)<1e-12
print('PASS PV02.02')
