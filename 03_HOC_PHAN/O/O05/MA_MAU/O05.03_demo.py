# coding: utf-8
# Bài O05.03 — Tài liệu có thể thực thi độc lập
from pathlib import PurePosixPath
p=PurePosixPath('dist/tool-0.1.0-py3-none-any.whl')
assert p.name.endswith('.whl')
