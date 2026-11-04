# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import math

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if type(value) not in (int, float):
            raise TypeError('nhiệt độ phải là số')
        if not math.isfinite(value) or value < -273.15:
            raise ValueError('nhiệt độ ngoài miền hợp lệ')
        self._celsius = float(value)

    @property
    def kelvin(self):
        return self._celsius + 273.15

def check():
    t = Temperature(0)
    assert math.isclose(t.kelvin, 273.15, abs_tol=1e-10)
    t.celsius = -273.15
    assert math.isclose(t.kelvin, 0, abs_tol=1e-10)
    try: t.celsius = float('nan')
    except ValueError: pass
    else: raise AssertionError('NaN phải bị từ chối')
    try: t.kelvin = 1
    except AttributeError: pass
    else: raise AssertionError('kelvin phải là read-only')

if __name__ == '__main__':
    check()
    print('OK E03.01', Temperature(0).kelvin)
