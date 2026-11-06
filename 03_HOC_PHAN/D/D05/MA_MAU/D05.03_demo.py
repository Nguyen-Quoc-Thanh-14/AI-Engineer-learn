# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def tao_thong_bao(ten: str, ngay: str) -> str:
    return f'{ngay}: Xin chào {ten.strip()}'
assert tao_thong_bao(' An ','02/11') == '02/11: Xin chào An'
print(tao_thong_bao('Binh','03/11'))
