# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def doc_so_luong(text):
    try:
        value = int(text.strip())
    except ValueError as exc:
        raise ValueError("phải nhập số nguyên") from exc
    if not 0 <= value <= 100:
        raise ValueError("ngoài [0, 100]")
    return value
print(doc_so_luong(" 12 "))
