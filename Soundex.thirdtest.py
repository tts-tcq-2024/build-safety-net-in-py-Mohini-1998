import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_four_character(self):
        self.assertEqual(generate_soundex("FGTM"), "F235")
        
    def test_four_character(self):
        self.assertEqual(generate_soundex("PJNR"), "P256") 
            
if __name__ == '__main__':
    unittest.main()
