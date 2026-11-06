# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from pathlib import Path

thu_muc_hien_tai = Path.cwd()
print("Đã xác định thư mục:", isinstance(thu_muc_hien_tai, Path))
