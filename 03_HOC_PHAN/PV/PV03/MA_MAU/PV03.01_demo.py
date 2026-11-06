# coding: utf-8
# Bài PV03.01 — Tài liệu có thể thực thi độc lập
from PIL import Image,ImageOps
img=Image.new('L',(4,2),color=128)
assert ImageOps.mirror(img).size==img.size
