import unittest
from my_calculator1 import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2), 2)
        self.assertEqual(self.calculator.add(2,3),5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1), -1)
        self.assertEqual(self.calculator.subtract(1,3), -2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3), 0)
        self.assertEqual(self.calculator.multiply(3,2), 6)
        self.assertEqual(self.calculator.multiply(-3,-2), 6)


    def test_divide(self):
        self.assertEqual(self.calculator.divide(2), 0)
        self.assertEqual(self.calculator.divide(2,2), 1)
 
    
    def test_nth_root(self):
        result = self.calculator.nth_root(2, 9)
        self.assertAlmostEqual(result, 3.0, places=2)

        with self.assertRaises(ValueError):
            self.calculator.nth_root(0, 9)

        with self.assertRaises(ValueError):
            self.calculator.nth_root(2, -9)

        with self.assertRaises(ValueError):
            self.calculator.nth_root(2, 9, -1)

    def test_reset(self):
        self.assertEqual(self.calculator.reset(), 0)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
