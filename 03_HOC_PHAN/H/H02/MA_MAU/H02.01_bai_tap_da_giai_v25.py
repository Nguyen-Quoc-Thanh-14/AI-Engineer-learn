"""H02.01 corrected: unittest for stock deduction (ordinary, zero, negative)."""
import unittest

def deduct_stock(available: int, quantity: int) -> int:
    if type(available) is not int or type(quantity) is not int:
        raise TypeError("stock and quantity must be int, not bool")
    if available < 0 or quantity < 0:
        raise ValueError("stock and quantity must be nonnegative")
    if quantity > available:
        raise ValueError("insufficient stock")
    return available - quantity

class InventoryTests(unittest.TestCase):
    def test_normal_purchase(self):
        self.assertEqual(deduct_stock(10, 3), 7)
    def test_zero_quantity(self):
        self.assertEqual(deduct_stock(10, 0), 10)
    def test_negative_quantity(self):
        with self.assertRaises(ValueError):deduct_stock(10, -1)
    def test_insufficient_stock(self):
        with self.assertRaises(ValueError):deduct_stock(3, 4)
    def test_boolean_quantity(self):
        with self.assertRaises(TypeError):deduct_stock(4, True)

def check():
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(InventoryTests)
    result=unittest.TestResult()
    suite.run(result)
    assert result.wasSuccessful() and result.testsRun==5, result.errors
if __name__=="__main__":
    check()
    print("PASS H02.01 inventory unittest")
