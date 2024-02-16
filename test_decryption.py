import unittest
from caesar import caesar 

class TestDecryption(unittest.TestCase):

   def test_decryption(self):
        # Test decryption with valid inputs
        self.assertEqual(caesar('def', 3, 'd'), 'abc')

        # Test decryption with shift of 0
        self.assertEqual(caesar('abc', 0, 'd'), 'abc')

        # Test decryption with shift of 25
        self.assertEqual(caesar('zab', 25, 'd'), 'abc')
        
if __name__ == '__main__':
    unittest.main()