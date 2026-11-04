# coding: utf-8
# Bài K05.03 — Tài liệu có thể thực thi độc lập
import time
start_wall=time.perf_counter();start_cpu=time.process_time()
time.sleep(.001)
assert time.perf_counter()-start_wall>=.001
assert time.process_time()-start_cpu>=0
