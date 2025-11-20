import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(7, 2), 9)
        self.assertEqual(self.calc.add(3, -2), 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(12, 4), 8)
        self.assertEqual(self.calc.subtract(3, 7), -4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 7), 14)
        self.assertEqual(self.calc.multiply(0, 4), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(22, 2), 11)
        self.assertAlmostEqual(self.calc.divide(11, 2), 5.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(1, 3), 1)
        self.assertEqual(self.calc.power(7, 0), 1)

if __name__ == '__main__':
    unittest.main()