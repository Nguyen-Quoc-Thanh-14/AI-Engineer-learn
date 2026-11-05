# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class TaiKhoan:
    def __init__(self, so_du): self.so_du=so_du

tk=TaiKhoan(100)
assert tk.so_du==100
print(tk.so_du)
