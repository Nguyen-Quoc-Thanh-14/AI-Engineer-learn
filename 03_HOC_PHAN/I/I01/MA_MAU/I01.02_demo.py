# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
values=[2,3,5,7,11]
queries=[3,4,5]
lookup=set(values)
assert [q in values for q in queries]==[q in lookup for q in queries]
print([q in lookup for q in queries])
