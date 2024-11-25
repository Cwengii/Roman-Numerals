import unittest

from roman_numerals import to_roman_numeral

class TestRomanNumerals(unittest.TestCase):
    
    def test_singles(self):
        self.assertEqual(to_roman_numeral(1),"I")
        self.assertEqual(to_roman_numeral(5),'V')
        
    def test_doubles(self):
        self.assertEqual(to_roman_numeral(10),'X')
        self.assertEqual(to_roman_numeral(50),'L')
        
    def test_hundreds(self):
        self.assertEqual(to_roman_numeral(100),'C')
        self.assertEqual(to_roman_numeral(500),'D')
 
    def test_thousands(self):
        self.assertEqual(to_roman_numeral(1000),'M')
        
if __name__ == '_main_':
    unittest.main()
