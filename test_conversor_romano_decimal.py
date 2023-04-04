import unittest
from conversor_romano_decimal import roman_to_decimal
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)
    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)
    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)
    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)
    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)
    def test_XL(self):
        resultado = roman_to_decimal('XL')
        self.assertEqual(resultado, 40)
    def test_L(self):
        resultado = roman_to_decimal('L')
        self.assertEqual(resultado, 50)
    def test_C(self):
        resultado = roman_to_decimal('C')
        self.assertEqual(resultado, 100)
    def test_D(self):
        resultado = roman_to_decimal('D')
        self.assertEqual(resultado, 500)
    def test_M(self):
        resultado = roman_to_decimal('M')
        self.assertEqual(resultado, 1000)
    



        
    
    
if __name__ == '__main__':
    unittest.main()