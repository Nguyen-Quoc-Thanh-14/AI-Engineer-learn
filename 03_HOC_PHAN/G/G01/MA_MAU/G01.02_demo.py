# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from pathlib import Path
p=Path('du_lieu')/'report.csv'
assert p.suffix=='.csv'
print(p.name)
