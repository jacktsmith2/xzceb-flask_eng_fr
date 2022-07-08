import unittest

from translator import englishToFrench, frenchToEnglish
from translator import englishText, frenchText

class Tests(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(englishText),'This is python programming')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(frenchText),'Il s agit d une programmation Python')

if __name__=='__main__':
    unittest.main() 