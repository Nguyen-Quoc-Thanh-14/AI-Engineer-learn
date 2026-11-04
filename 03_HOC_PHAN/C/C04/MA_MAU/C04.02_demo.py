# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
ten = ["An", "Bình", "Chi"]
diem = [9, 7, 9]
print(list(enumerate(ten, start=1)))
print(sorted(zip(ten, diem), key=lambda x: (-x[1], x[0])))
