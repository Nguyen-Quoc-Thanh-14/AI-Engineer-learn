# coding: utf-8
# Bài G04.02 — Tài liệu có thể thực thi độc lập
import os, tempfile
from pathlib import Path
with tempfile.TemporaryDirectory() as d:
    final = Path(d) / 'out.txt'
    tmp = Path(d) / 'tmp.txt'
    tmp.write_text('complete', encoding='utf-8')
    os.replace(tmp, final)
    assert final.read_text(encoding='utf-8') == 'complete'
