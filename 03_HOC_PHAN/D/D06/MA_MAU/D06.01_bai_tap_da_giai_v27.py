# coding: utf-8
# Bài B D06.01: sử dụng cú pháp type parameter PEP 695 (Python >= 3.12).
def first[T](items: list[T]) -> T:
    if not items:
        raise ValueError("danh sách không được rỗng")
    return items[0]

assert first([5, 9]) == 5
assert first(["x", "y"]) == "x"
try:
    first([])
except ValueError:
    pass
else:
    raise AssertionError("phải từ chối danh sách rỗng")

print("PASS D06.01")
