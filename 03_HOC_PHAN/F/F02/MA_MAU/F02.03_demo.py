# coding: utf-8
# Bài F02.03 — Tài liệu có thể thực thi độc lập
import tomllib
config = tomllib.loads("[project]\nname = 'example-tool'\nversion = '0.1.0'")
assert config['project']['name'] == 'example-tool'
