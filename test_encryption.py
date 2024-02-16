import unittest
from caesar import caesar 

class TestEncryption(unittest.TestCase):

    def test_encryption(self):
        # Test encryption with valid inputs
        self.assertEqual(caesar('abc', 3, 'e'), 'def')

        # Test encryption with shift of 0
        self.assertEqual(caesar('abc', 0, 'e'), 'abc')

        # Test encryption with shift of 25
        self.assertEqual(caesar('abc', 25, 'e'), 'zab')

if __name__ == '__main__':
    unittest.main()