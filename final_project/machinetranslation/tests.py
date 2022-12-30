"""Module providing e2f f2e translator tests."""
import unittest
from translator import englishtofrench, frenchtoenglish

class Testtranslator(unittest.TestCase):
    def test_f2e(self):
        #self.assertIsNone(inputfrenchtext)
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
    def test_e2f(self):
        #self.assertIsNone(inputenglishtext)
        self.assertEqual(englishtofrench('Hello'),'Bonjour')

if __name__=='__main__':
    unittest.main()



