# coding: utf-8
# Bài F02.01 — Tài liệu có thể thực thi độc lập
from pathlib import PurePosixPath
src = PurePosixPath('project/src/app/core.py')
assert src.parts[:3] == ('project', 'src', 'app')
assert src.suffix == '.py'
