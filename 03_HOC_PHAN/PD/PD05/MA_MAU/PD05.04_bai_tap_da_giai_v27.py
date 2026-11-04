# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
chunks=[[1,2,3],[100]]
wrong=sum(sum(c)/len(c) for c in chunks)/len(chunks)
correct=sum(map(sum,chunks))/sum(map(len,chunks))
assert wrong==51
assert correct==26.5
assert wrong!=correct
print('PASS PD05.04')
