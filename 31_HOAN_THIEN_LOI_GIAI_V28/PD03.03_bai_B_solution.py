import pandas as pd
# DST gap in New York: 2 AM local time is skipped on 2026-03-08.
idx=pd.date_range('2026-03-08 00:00',periods=5,freq='h',tz='America/New_York')
assert '02:00' not in [x.strftime('%H:%M') for x in idx]
counts=pd.Series([1]*len(idx),index=idx).resample('h').sum()
assert len(counts)==5
