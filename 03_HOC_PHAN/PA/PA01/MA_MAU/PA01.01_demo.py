# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from tempfile import TemporaryDirectory
from pathlib import Path
with TemporaryDirectory() as d:
    p=Path(d)
    (p/'a.txt').write_text('a')
    (p/'b.csv').write_text('x,y')
    counts={ext:sum(x.suffix==ext for x in p.iterdir()) for ext in ['.txt','.csv']}
    assert counts=={'.txt':1,'.csv':1}
