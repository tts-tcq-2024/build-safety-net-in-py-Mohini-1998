import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):
    
    def test_four_character(self):
        self.assertEqual(generate_soundex("BFPV"), "B000")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BCDL"), "B234")


if __name__ == '__main__':
    unittest.main()
