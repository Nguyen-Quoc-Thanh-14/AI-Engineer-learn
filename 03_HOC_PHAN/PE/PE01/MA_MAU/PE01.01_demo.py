# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
events=[{'id':1,'x':2},{'id':2,'x':3},{'id':1,'x':2}]
seen=set();out=[]
for e in events:
    if e['id'] not in seen:
        seen.add(e['id']);out.append(e)
assert [e['id'] for e in out]==[1,2]
print(len(out))
