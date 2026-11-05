# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def phan_tich_lenh(cmd):
    match cmd:
        case ("add", x, y) if isinstance(x, int) and isinstance(y, int):
            return x + y
        case ("quit",):
            return "bye"
        case _:
            return "unknown"
print(phan_tich_lenh(("add", 2, 3)))
print(phan_tich_lenh(("quit",)))
