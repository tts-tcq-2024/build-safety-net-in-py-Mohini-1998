import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
  
    def test_four_character(self):
        self.assertEqual(generate_soundex("BCDLM"), "B234")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BDLMNR"), "B345") 
        
if __name__ == '__main__':
    unittest.main()
