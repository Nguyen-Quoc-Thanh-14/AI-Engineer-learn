# coding: utf-8
# Bài N02.01 — Tài liệu có thể thực thi độc lập
import os
os.environ['COURSE_DUMMY_TOKEN']='not-real'
try:
    value=os.environ['COURSE_DUMMY_TOKEN']
    assert value=='not-real'
finally:
    os.environ.pop('COURSE_DUMMY_TOKEN',None)
