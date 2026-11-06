# coding: utf-8
# Bài G01.03 — Tài liệu có thể thực thi độc lập
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as d:
    p = Path(d) / 'item.txt'
    p.write_text('abc', encoding='utf-8')
    assert p.read_text(encoding='utf-8') == 'abc'
    assert p.is_file()
