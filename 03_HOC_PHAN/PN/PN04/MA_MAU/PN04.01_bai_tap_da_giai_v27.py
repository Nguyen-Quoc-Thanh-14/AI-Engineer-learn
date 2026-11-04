# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
def chunk_utf8(text,max_bytes):
    if max_bytes<=0:raise ValueError
    data=text.encode('utf-8');result=[];start=0
    for word in text.split():
        b=word.encode('utf-8')
        if len(b)>max_bytes:raise ValueError('word too long')
    while start<len(data):
        end=min(start+max_bytes,len(data))
        while end>start:
            try:data[start:end].decode('utf-8');break
            except UnicodeDecodeError:end-=1
        if end==start:raise ValueError
        result.append((start,end,data[start:end].decode('utf-8')));start=end
    return result
result=chunk_utf8('á bc',3)
assert b''.join(x[2].encode('utf-8') for x in result)=='á bc'.encode('utf-8')
assert result[0][0]==0
assert all((e-s)<=3 for s,e,_ in result)
print('PASS PN04.01')
