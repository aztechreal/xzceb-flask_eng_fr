"""Module providing e2f f2e translator tests."""
import unittest
from translator import englishtofrench, frenchtoenglish

class Testtranslator(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(frenchtoenglish(''),'') #check null input
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchtoenglish('Bonjour'),'Bye')
    def test_e2f(self):
        self.assertEqual(englishtofrench(''),'') #check null input
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('Hello'),'Adieu')
if __name__=='__main__':
    unittest.main()



