# coding: utf-8
# Bài F04.02 — Tài liệu có thể thực thi độc lập
import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Config: port: int
raw=os.getenv('COURSE_PORT','8080')
conf=Config(int(raw));assert 1<=conf.port<=65535
