# coding: utf-8
# Bài PA01.03 — Tài liệu có thể thực thi độc lập
import argparse
p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=1)
assert p.parse_args(['--count','3']).count==3
