# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def so_phan_tu_duoc_sao_chep(n):
    capacity=1; copies=0
    for length in range(n):
        if length==capacity:
            copies+=length
            capacity*=2
    return copies
assert so_phan_tu_duoc_sao_chep(1)==0
assert so_phan_tu_duoc_sao_chep(8)<2*8
