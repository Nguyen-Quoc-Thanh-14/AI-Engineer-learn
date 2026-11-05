# coding: utf-8
# Bài O01.03 — Tài liệu có thể thực thi độc lập
import sys, os
assert os.path.isabs(sys.executable)
assert sys.version_info.major==3
