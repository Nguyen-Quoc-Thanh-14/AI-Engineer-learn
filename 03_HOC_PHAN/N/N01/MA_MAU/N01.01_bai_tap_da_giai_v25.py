# -*- coding: utf-8 -*-
"""N01.01: score schema 0..10 with non-finite and wrong-type rejection.
This is the corrected answer to the exercise; filename retained for existing links.
"""
import math


def parse_score(value: object) -> float:
    """Accept only builtin int/float between 0 and 10; reject bool, NaN, infinities.

    This contract intentionally DOES NOT coerce strings or Decimal.
    """
    if type(value) not in (int, float):
        raise TypeError("Điểm phải là int hoặc float; không nhận bool/chuỗi")
    if not 0 <= value <= 10:
        raise ValueError("Điểm phải nằm trong [0, 10] và không là NaN")
    if type(value) is float and not math.isfinite(value):
        raise ValueError("Điểm phải hữu hạn")
    return float(value)


def check() -> None:
    for raw, expected in [(0, 0.0), (10, 10.0), (7.5, 7.5), (-0.0, 0.0)]:
        assert parse_score(raw) == expected
    for raw in (float("nan"), float("inf"), -float("inf"), -0.01, 10.00001, 10**500):
        try:
            parse_score(raw)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Phải từ chối giá trị ngoài miền: {raw!r}")
    for raw in (True, False, "7", None, [], {"score": 7}):
        try:
            parse_score(raw)
        except TypeError:
            pass
        else:
            raise AssertionError(f"Phải từ chối kiểu không hợp lệ: {raw!r}")


if __name__ == "__main__":
    check()
    print("PASS N01.01 score validation")
