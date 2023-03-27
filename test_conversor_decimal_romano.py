import unittest
def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return 'IV'
    elif decimal in range (5,9):
        return 'V'+ decimal_to_roman(decimal-5)
    elif decimal == 9: 
        return 'IX'
    elif decimal in range (10,40):
        return (('X'*(decimal//10))+decimal_to_roman(decimal %10))
    elif decimal in range (40,50):
        return ('XL'+decimal_to_roman(decimal%40))
    elif decimal in range (50,90):
        return ('L'+ decimal_to_roman(decimal -50))
    elif decimal in range (90,100):
        return ('XC'+ decimal_to_roman(decimal-90))
    elif decimal in range (100,400):
        return (('C'* (decimal //100)) + decimal_to_roman(decimal%100))
    elif decimal in range (400,500):
        return ('CD' + decimal_to_roman(decimal-400))
    elif decimal in range (500,900):
        return ('D'+ decimal_to_roman(decimal-500))
    elif decimal in range (900,1000):
        return ('CM' + decimal_to_roman(decimal-900))
    elif decimal ==1000:
        return 'M'


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