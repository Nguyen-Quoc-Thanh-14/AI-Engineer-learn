# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import timeit
samples=timeit.repeat('sum(range(100))',number=100,repeat=3)
assert len(samples)==3
assert all(x>=0 for x in samples)
print('số mẫu:',len(samples))
