# coding: utf-8
# Lời giải vận dụng riêng; CPython 3.13.5 (lịch sử), 3.15.2 (Actions #42232418794) PASS; chưa phản biện độc lập
from typing import Optional
def normalize(value: Optional[str]) -> str:
    if value is not None:
        return value.strip().upper()  # nhánh này đã narrowing từ Optional[str] thành str
    return 'UNKNOWN'
assert normalize(' abc ') == 'ABC'
assert normalize('') == ''
assert normalize(None) == 'UNKNOWN'
# Tĩnh: chạy mypy/pyright ngoài tập thử runtime mới kiểm chứng được narrowing.
print('PASS D06.04')
