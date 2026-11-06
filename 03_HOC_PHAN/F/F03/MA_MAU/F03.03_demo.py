# coding: utf-8
# Bài F03.03 — Tài liệu có thể thực thi độc lập
from pathlib import PurePosixPath
wheel = PurePosixPath('demo_pkg-0.1.0-py3-none-any.whl')
sdist = PurePosixPath('demo_pkg-0.1.0.tar.gz')
assert wheel.suffix == '.whl'
assert sdist.name.endswith('.tar.gz')
