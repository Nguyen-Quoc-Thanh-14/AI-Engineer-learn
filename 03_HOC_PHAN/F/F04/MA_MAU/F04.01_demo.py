# coding: utf-8
# Bài F04.01 — Tài liệu có thể thực thi độc lập
import logging, io
stream=io.StringIO(); handler=logging.StreamHandler(stream)
logger=logging.getLogger('course.F04');logger.addHandler(handler);logger.setLevel(logging.INFO)
logger.info('processed=%s',4)
assert 'processed=4' in stream.getvalue()
logger.removeHandler(handler)
