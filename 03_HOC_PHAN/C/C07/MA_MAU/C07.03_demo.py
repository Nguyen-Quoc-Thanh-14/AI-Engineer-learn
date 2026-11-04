# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
# Chỉ chạy với Python 3.15+
MISSING = sentinel("MISSING")
data = {"x": None}
print(data.get("x", MISSING) is MISSING)
print(data.get("y", MISSING) is MISSING)
