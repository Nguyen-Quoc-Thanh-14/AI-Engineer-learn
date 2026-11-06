import time,statistics
measure=[]
for _ in range(5):
    w=time.perf_counter();p=time.process_time()
    sum(i*i for i in range(100000))
    measure.append((time.perf_counter()-w,time.process_time()-p))
assert len(measure)==5 and all(w>0 and p>0 for w,p in measure)
print('median wall/cpu seconds',tuple(statistics.median(x) for x in zip(*measure)))
