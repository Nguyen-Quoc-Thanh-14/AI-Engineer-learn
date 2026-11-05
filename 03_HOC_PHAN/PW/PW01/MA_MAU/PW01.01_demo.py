# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
from http import HTTPStatus
assert HTTPStatus.OK==200
assert HTTPStatus.BAD_REQUEST==400
assert HTTPStatus.INTERNAL_SERVER_ERROR==500
print(HTTPStatus.OK.phrase)
