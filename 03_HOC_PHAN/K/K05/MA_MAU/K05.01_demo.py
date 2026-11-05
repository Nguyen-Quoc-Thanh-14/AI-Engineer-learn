# coding: utf-8
# Bài K05.01 — Tài liệu có thể thực thi độc lập
import cProfile, pstats, io
prof=cProfile.Profile();prof.enable();sum(range(100));prof.disable()
s=io.StringIO();pstats.Stats(prof,stream=s).sort_stats('cumulative').print_stats(3)
assert s.getvalue()
