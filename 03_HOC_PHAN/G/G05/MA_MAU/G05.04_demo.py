# coding: utf-8
# Bài G05.04 — Tài liệu có thể thực thi độc lập
from pathlib import PurePosixPath
root = PurePosixPath('/safe')
relative = PurePosixPath('folder/file.txt')
assert '..' not in relative.parts
assert (root / relative).as_posix() == '/safe/folder/file.txt'
