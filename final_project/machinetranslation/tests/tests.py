import unittest
from translator import english_to_french, french_to_english

class TestMachineTranslation(unittest.TestCase):

    def test_french_to_english_null(self):
        self.assertEqual(french_to_english(''), None)

    def test_english_to_french_null(self):
        self.assertEqual(english_to_french(''), None)

    def test_french_to_english_0(self):
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')
    
    def test_french_to_english_1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french_0(self):
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')

    def test_english_to_french_1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()