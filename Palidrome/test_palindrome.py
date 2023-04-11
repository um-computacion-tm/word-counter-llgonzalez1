import unittest
from palindrome import palindrome
class TestPalindrome(unittest.TestCase):
    def test_palabra_simple_true(self):
        result= palindrome('neuquen')
        self.assertEqual(result, True)
    def test_palabra_simple_false(self):
        result= palindrome('computacion')
        self.assertEqual(result, False)
    def test_palabra_complex_true(self):
        result= palindrome('ojo rojo ')
        self.assertEqual(result, True)
    def test_palabra_complex_false(self):
        result= palindrome('ojo rojo grande ')
        self.assertEqual(result, False)    


   

if __name__ == '__main__':
    unittest.main()