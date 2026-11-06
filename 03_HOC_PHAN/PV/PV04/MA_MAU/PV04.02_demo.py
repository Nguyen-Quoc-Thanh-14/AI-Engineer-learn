# coding: utf-8
# Bài PV04.02 — Tài liệu có thể thực thi độc lập
mask_a={1,2,3};mask_b={2,3,4}
iou=len(mask_a&mask_b)/len(mask_a|mask_b)
assert iou==.5
