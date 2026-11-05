# coding: utf-8
# Lời giải vận dụng riêng, Python 3.13.5; 3.15.2 chưa thực thi
from datetime import datetime,timedelta,timezone
now=datetime(2026,11,3,tzinfo=timezone.utc)
records=[('a',now),('b',now-timedelta(hours=3)),('a',now)]
ids=[id for id,_ in records]
report={'total':len(records),'duplicate_ids':len(ids)-len(set(ids)),
    'stale_rows':sum(now-ts>timedelta(hours=2) for _,ts in records)}
assert report=={'total':3,'duplicate_ids':1,'stale_rows':1}
assert report['total']>=report['duplicate_ids']
print('PASS PE01.03')
