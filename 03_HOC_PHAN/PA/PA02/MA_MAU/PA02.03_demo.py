# coding: utf-8
# Bài PA02.03 — Tài liệu có thể thực thi độc lập
from datetime import datetime,timedelta,timezone
now=datetime(2026,1,1,tzinfo=timezone.utc)
assert now+timedelta(days=1)>now
