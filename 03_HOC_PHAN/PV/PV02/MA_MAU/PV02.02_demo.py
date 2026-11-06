# coding: utf-8
# Bài PV02.02 — Tài liệu có thể thực thi độc lập
def iou(a,b):
    ix=max(0,min(a[2],b[2])-max(a[0],b[0]))
    iy=max(0,min(a[3],b[3])-max(a[1],b[1]))
    inter=ix*iy
    return inter/((a[2]-a[0])*(a[3]-a[1])+(b[2]-b[0])*(b[3]-b[1])-inter)
assert iou((0,0,2,2),(0,0,2,2))==1
