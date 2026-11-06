# coding: utf-8
# Bản sao mã ví dụ v2.6 được đưa về đúng vị trí bài học; không phải lời giải B.
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+3,5)
case=TestMath('test_add')
res=unittest.TestResult(); case.run(res)
assert res.wasSuccessful()
