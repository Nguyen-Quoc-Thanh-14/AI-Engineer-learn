import ctypes,time,statistics
# Calling the process C runtime repeatedly incurs Python/native boundary overhead.
libc=ctypes.CDLL(None)
strlen=libc.strlen;strlen.argtypes=[ctypes.c_char_p];strlen.restype=ctypes.c_size_t
payloads=[b'hello']*1000
assert sum(strlen(x) for x in payloads)==5000
assert len(b''.join(payloads))==5000
# These are *different operations*; benchmark only for boundary overhead exploration, not speed equivalence.
samples=[]
for _ in range(5):
    t=time.perf_counter();sum(strlen(x) for x in payloads);samples.append(time.perf_counter()-t)
assert statistics.median(samples)>0
