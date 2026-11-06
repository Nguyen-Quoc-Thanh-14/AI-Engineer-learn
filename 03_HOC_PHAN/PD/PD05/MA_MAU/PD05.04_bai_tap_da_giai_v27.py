# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
chunks=[[1,2,3],[100]]
wrong=sum(sum(c)/len(c) for c in chunks)/len(chunks)
correct=sum(map(sum,chunks))/sum(map(len,chunks))
assert wrong==51
assert correct==26.5
assert wrong!=correct
print('PASS PD05.04')
