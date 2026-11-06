# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from collections.abc import Mapping
print(isinstance({"x": 1}, Mapping))
print(isinstance([1], Mapping))
