# coding: utf-8
# Bài O06.02 — Tài liệu có thể thực thi độc lập
import sys
markers={'python_version':f'{sys.version_info.major}.{sys.version_info.minor}'}
assert markers['python_version'].count('.')==1
