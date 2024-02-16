import unittest
from caesar import caesar 

class TestInvalidShift(unittest.TestCase):

   def test_invalid_shift(self):
        
     # Test decryption with invalid shift
     self.assertEqual(caesar('abc', -1, 'd'), 'invalid shift')
     self.assertEqual(caesar('abc', 26, 'd'), 'invalid shift')
     self.assertEqual(caesar('abc', 'a', 'd'), 'invalid shift')

     # Test encryption with invalid shift
     self.assertEqual(caesar('abc', -1, 'e'), 'invalid shift')
     self.assertEqual(caesar('abc', 26, 'e'), 'invalid shift')
     self.assertEqual(caesar('abc', 'a', 'e'), 'invalid shift')

        
if __name__ == '__main__':
    unittest.main()
