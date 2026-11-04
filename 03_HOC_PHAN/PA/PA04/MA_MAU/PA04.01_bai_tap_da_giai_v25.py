# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
from pathlib import Path
from tempfile import TemporaryDirectory

def rename_txt(folder: Path, *, apply: bool = False) -> list[tuple[Path, Path]]:
    folder = Path(folder)
    if not folder.is_dir():
        raise NotADirectoryError(folder)
    changes = []
    for source in sorted(folder.iterdir()):
        if not source.is_file() or source.suffix != '.TXT':
            continue
        dest = source.with_suffix('.txt')
        if dest.exists():
            raise FileExistsError(dest)
        changes.append((source, dest))
    if apply:
        for source, dest in changes:
            source.rename(dest)
    return changes

def check():
    with TemporaryDirectory() as temp:
        folder = Path(temp)
        (folder / 'a.TXT').write_text('hello', encoding='utf-8')
        plan = rename_txt(folder)
        assert len(plan) == 1 and (folder/'a.TXT').exists()
        assert len(rename_txt(folder, apply=True)) == 1
        assert rename_txt(folder, apply=True) == []  # idempotent với input này
        assert (folder/'a.txt').read_text(encoding='utf-8') == 'hello'
        (folder/'b.TXT').write_text('source')
        (folder/'b.txt').write_text('target')
        try: rename_txt(folder, apply=True)
        except FileExistsError: pass
        else: raise AssertionError('phải phát hiện collision')

if __name__ == '__main__':
    check()
    print('OK PA04.01')
