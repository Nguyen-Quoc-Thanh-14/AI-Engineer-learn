# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
import csv,io
raw='id,qty\na,2\nb,-3\nc,4\n'
rows=list(csv.DictReader(io.StringIO(raw)));valid=[];invalid=[]
for row in rows:
    try:
        q=int(row['qty'])
        if q<0:raise ValueError
        valid.append((row['id'],q))
    except ValueError:invalid.append(row)
assert len(rows)==3
assert valid==[('a',2),('c',4)]
assert len(invalid)==1 and invalid[0]['id']=='b'
print('PASS PD04.02')
