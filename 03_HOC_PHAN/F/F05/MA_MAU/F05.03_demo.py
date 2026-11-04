# coding: utf-8
# Bài F05.03 — Tài liệu có thể thực thi độc lập
# Kiểm tra hành vi nền tảng chung, không mô phỏng tính năng 3.15.
import importlib.util
assert importlib.util.find_spec('json') is not None
