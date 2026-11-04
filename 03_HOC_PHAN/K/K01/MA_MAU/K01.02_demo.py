# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import cProfile, pstats, io
p=cProfile.Profile()
p.enable()
sum(i*i for i in range(1000))
p.disable()
out=io.StringIO()
pstats.Stats(p,stream=out).sort_stats('cumtime').print_stats(3)
assert 'function calls' in out.getvalue()
