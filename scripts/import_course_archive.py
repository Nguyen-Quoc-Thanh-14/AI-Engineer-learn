#!/usr/bin/env python3
"""Secure-ish content importer for a tightly scoped course archive already on GitHub.
Checks both outer archive digest and every member SHA256 before writing any source.
"""
import csv,hashlib,io,os,pathlib,tarfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'source'/'full-course-536-v31.tar.xz'
EXPECTED_ARCHIVE_SHA256='8335d53e8428c3f231158c898d6357b14fe7d0c9e2fa6104364a6c22e45361d5'
EXPECTED_COUNTS={'lessons':441,'demos':441,'solutions':95}
ROOTS=('03_HOC_PHAN/','31_HOAN_THIEN_LOI_GIAI_V28/','35_KIEM_DINH_CPYTHON_3152/','37_KIEM_DINH_V31/')
METADATA={'GITHUB_PACKAGE_MANIFEST.json','GITHUB_SOURCE_SHA256.csv','GITHUB_UPLOAD_INSTRUCTIONS.md','GITHUB_REVIEW_MATRIX.csv'}
EXTENSIONS={'.py','.md','.csv','.json','.txt'}

def main():
    assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()==EXPECTED_ARCHIVE_SHA256,'ARCHIVE_SHA256_MISMATCH'
    data={}
    with tarfile.open(ARCHIVE,mode='r:xz') as archive:
        for member in archive.getmembers():
            name=member.name
            path=pathlib.PurePosixPath(name)
            assert member.isfile(),f'NOT_REGULAR_FILE: {name}'
            assert name not in data,f'DUPLICATE_PATH: {name}'
            assert not path.is_absolute() and '..' not in path.parts and '\\' not in name,f'UNSAFE_PATH: {name}'
            assert name.startswith(ROOTS) or name in METADATA,f'UNEXPECTED_SOURCE: {name}'
            assert pathlib.Path(name).suffix in EXTENSIONS,f'UNEXPECTED_EXTENSION: {name}'
            assert '/__pycache__/' not in name and '/.git/' not in name,f'UNEXPECTED_CACHE: {name}'
            data[name]=archive.extractfile(member).read()
    assert len(data)==1919, f'ARCHIVE_FILE_COUNT {len(data)} != 1919'
    manifest={row['path']:row for row in csv.DictReader(io.StringIO(data['GITHUB_SOURCE_SHA256.csv'].decode('utf-8-sig')))}
    for name,b in data.items():
        b.decode('utf-8-sig')  # no unknown binary content
        if name not in METADATA:
            row=manifest.get(name)
            assert row is not None, f'MANIFEST_ENTRY_MISSING: {name}'
            assert hashlib.sha256(b).hexdigest()==row['sha256'] and len(b)==int(row['size_bytes']), f'FILE_TAMPERED: {name}'
    count={
     'lessons':sum('/BAI_HOC/' in n and n.endswith('.md') for n in data),
     'demos':sum('/MA_MAU/' in n and n.endswith('_demo.py') for n in data),
     'solutions':sum(n.startswith('31_HOAN_THIEN_LOI_GIAI_V28/') and n.endswith('_bai_B_solution.py') for n in data),
    }
    assert count==EXPECTED_COUNTS, f'WRONG_SOURCE_COUNTS {count}'
    # No writes until validation finishes; never modify source outside permitted paths.
    for name,b in data.items():
        dest=ROOT/pathlib.PurePosixPath(name)
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(b)
    print('IMPORTED_VERIFIED_COURSE',count,'total_files',len(data))

if __name__=='__main__':main()