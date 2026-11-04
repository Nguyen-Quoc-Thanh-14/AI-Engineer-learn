# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
# Chỉ chạy với CPython 3.15+
d = frozendict({"env": "prod", "retry": 3})
print(d["retry"])
print(hash(d) == hash(frozendict({"retry": 3, "env": "prod"})))
