import unittest
from contador_palabras import count_words
class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})
    def test_complex(self):
        result = count_words('chau mundo')
        self.assertEqual(result, {'chau': 1, 'mundo':1})
    def test_very_complex(self):
        result = count_words('pablito clavo un clavito que clavito clavo pablito')
        self.assertEqual(result, {'pablito': 2, 'clavo':2, 'un':1, 'clavito':2, 'que':1 })
    def test_very_complex(self):
        result = count_words('pablito clavo un clavito que clavito clavo pablito')
        self.assertEqual(result, {'pablito': 2, 'clavo':2, 'un':1, 'clavito':2, 'que':1 })
    def test_very_complex_2(self):
        result = count_words('Tengo una gallina pinta , pipiripinta , pipirialegre y gorda , que tiene tres pollitos pintos , pipiripintos , pipirialegres y gordos . Si la gallina no hubiera sido pinta pipiripinta , pipirialegre y gorda ; los pollitos no hubieran sido pintos , pipiripintos , pipirialegres y gordos')
        self.assertEqual(result, {'Tengo': 1, 'una': 1, 'gallina': 2, 'pinta': 2, ',': 8, 'pipiripinta': 2, 'pipirialegre': 2, 'y': 4, 'gorda': 2, 'que': 1, 'tiene': 1, 'tres': 1, 'pollitos': 2, 'pintos': 2, 'pipiripintos': 2, 'pipirialegres': 2, 'gordos': 2, '.': 1, 'Si': 1, 'la': 1, 'no': 2, 'hubiera': 1, 'sido': 2, ';': 1, 'los': 1, 'hubieran': 1 })

if __name__ == '__main__':
    unittest.main()