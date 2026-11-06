# coding: utf-8
# Bài H04.02 — Tài liệu có thể thực thi độc lập
import logging, io
s = io.StringIO()
handler = logging.StreamHandler(s)
log = logging.getLogger('course_v24_h04')
log.handlers[:] = [handler]
log.setLevel(logging.INFO)
log.info('processed=%d', 3)
assert 'processed=3' in s.getvalue()
log.removeHandler(handler)
