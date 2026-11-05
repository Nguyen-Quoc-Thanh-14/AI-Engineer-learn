# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def xu_ly(du_lieu, phep_bien_doi):
    return [phep_bien_doi(x) for x in du_lieu]

def nhan_doi(x):
    return x * 2

assert xu_ly([2, 3], nhan_doi) == [4, 6]
assert xu_ly([], nhan_doi) == []
print(xu_ly([2, 3], nhan_doi))
