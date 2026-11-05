# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from scipy.optimize import minimize_scalar
res=minimize_scalar(lambda x:(x-2)**2)
assert res.success
assert abs(res.x-2)<1e-5
print(round(res.x,5))
