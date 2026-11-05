# coding: utf-8
# Bài J05.01 — Tài liệu có thể thực thi độc lập
import importlib, sys
m=importlib.import_module('json')
assert sys.modules['json'] is m
assert importlib.import_module('json') is m
