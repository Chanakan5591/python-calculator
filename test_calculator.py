import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(8, -4), 4)

    def test_add_negative_flipped(self):
        self.assertEqual(self.calc.add(-24, 32), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    
    def test_subtract_neg_flipped(self):
        self.assertEqual(self.calc.subtract(-500500, 1000000), -1500500)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 8), 32)
    
    def test_multiply_neg_flipped(self):
        self.assertEqual(self.calc.multiply(-9, 4), -36)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        
    def test_divide_neg_flipped(self):
        self.assertEqual(self.calc.divide(-4, 2), -2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(8, 12), 8)
    
    def test_modulo_neg_flipped(self):
        self.assertEqual(self.calc.modulo(-9, 55), 46)

if __name__ == '__main__':
    unittest.main()