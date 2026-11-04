# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
class LoiMa(Exception):pass

def parse_ma(s):
    try:return int(s)
    except ValueError as e:
        raise LoiMa('ma khong hop le') from e
try:parse_ma('x')
except LoiMa as e:
    assert isinstance(e.__cause__,ValueError)
else:raise AssertionError()
