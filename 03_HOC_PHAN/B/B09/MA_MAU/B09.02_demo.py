# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
def du_tuoi(tuoi):
    return tuoi >= 18
for age in (17, 18, 19):
    print(age, du_tuoi(age))
