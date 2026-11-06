# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from pathlib import Path
cwd=Path.cwd()
assert cwd.is_dir()
print('cwd:',cwd.name)
