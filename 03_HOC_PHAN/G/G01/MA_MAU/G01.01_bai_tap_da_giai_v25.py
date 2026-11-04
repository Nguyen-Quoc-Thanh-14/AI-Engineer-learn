# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from pathlib import Path
from tempfile import TemporaryDirectory

def write_text_file(path: Path, lines: list[str]) -> None:
    if not all(isinstance(x, str) for x in lines):
        raise TypeError('mỗi dòng phải là str')
    with Path(path).open('w', encoding='utf-8', newline='') as f:
        f.write(''.join(lines))

def read_text_file(path: Path) -> str:
    with Path(path).open('r', encoding='utf-8') as f:
        return f.read()

def check():
    with TemporaryDirectory() as tmp:
        dest = Path(tmp) / 'notes.txt'
        write_text_file(dest, ['Xin chào\n', 'Python!'])
        assert read_text_file(dest) == 'Xin chào\nPython!'
        write_text_file(dest, [])
        assert read_text_file(dest) == ''
        try: write_text_file(dest, [42])
        except TypeError: pass
        else: raise AssertionError('sai kiểu')

if __name__ == '__main__':
    check()
    print('OK G01.01')
