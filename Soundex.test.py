import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    #def test_empty_string(self):
        #self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BFPV"), "B000")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BCDL"), "B234")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("FGTM"), "F235")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("PJNR"), "P256") 
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("VKQS"), "V200")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("XZMN"), "X500")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BCDLM"), "B234")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("BDLMNR"), "B345") 
        
if __name__ == '__main__':
    unittest.main()
