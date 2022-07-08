#Test for translator

import unittest
from machinetranslation import translator
from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('null'), ' ')
        self.assertNotEqual(english_to_french(0), 0)

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('nulle'), ' ')
        self.assertNotEqual(french_to_english(0), 0)

unittest.main()