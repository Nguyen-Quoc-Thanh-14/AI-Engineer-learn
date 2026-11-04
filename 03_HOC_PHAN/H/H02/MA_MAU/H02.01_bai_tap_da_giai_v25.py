# -*- coding: utf-8 -*-
# Bài tập được giải riêng — Python v2.5
import unittest

def normalize_username(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError('name phải là str')
    result = name.strip().lower()
    if not result:
        raise ValueError('không được trống')
    return result

class UsernameTests(unittest.TestCase):
    def test_regular(self):
        # Arrange
        raw = '  Alice  '
        # Act
        result = normalize_username(raw)
        # Assert
        self.assertEqual(result, 'alice')

    def test_boundary(self):
        self.assertEqual(normalize_username(' A '), 'a')

    def test_invalid(self):
        with self.assertRaises(ValueError):
            normalize_username('   ')
        with self.assertRaises(TypeError):
            normalize_username(None)

def check():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UsernameTests)
    result = unittest.TestResult()
    suite.run(result)
    assert result.wasSuccessful() and result.testsRun == 3

if __name__ == '__main__':
    check()
    print('OK H02.01')
