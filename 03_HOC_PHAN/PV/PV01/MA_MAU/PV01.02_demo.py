# coding: utf-8
# Bài PV01.02 — Tài liệu có thể thực thi độc lập
from PIL import Image
img=Image.new('RGB',(3,2),(255,0,0))
assert img.size==(3,2) and img.getpixel((0,0))==(255,0,0)
