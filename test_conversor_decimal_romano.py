import unittest
from conversor_decimal_romano import decimal_to_roman
 

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, 'I')
    def test_Cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')
    def test_Cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')
    def test_Nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')
    def test_Diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')
    def test_Cuarenta(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')
    def test_Cincuenta(self):
        resultado = decimal_to_roman(50)
        self.assertEqual(resultado, 'L')
    def test_Noventa(self):
        resultado = decimal_to_roman(90)
        self.assertEqual(resultado, 'XC')
    def test_Cien(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')
    def test_Cuatricientos(self):
        resultado= decimal_to_roman(400)
        self.assertEqual(resultado, 'CD')
    def test_Quinientos(self):
        resultado= decimal_to_roman(500)
        self.assertEqual(resultado, 'D')
    def test_novecientos(self):
        resultado= decimal_to_roman(900)
        self.assertEqual(resultado, 'CM')
    def test_Mil(self):
        resultado= decimal_to_roman(1000)
        self.assertEqual(resultado, 'M')
        
    
if __name__ == '__main__':
    unittest.main()