import unittest
from caesar import caesar 

class TestInvalidOption(unittest.TestCase):

   def test_invalid_option(self):
      
      # Test invalid option with a non-standard operation character
      self.assertEqual(caesar("hello", 3, "x"), "invalid option")
      
      # Test invalid option with a number
      self.assertEqual(caesar("hello", 3, 3), "invalid option")
      
      # Test invalid option with a special character
      self.assertEqual(caesar("hello", 3, "!"), "invalid option")
      
      # Test invalid option with an empty operation string
      self.assertEqual(caesar("hello", 3, ""), "invalid option")

if __name__ == '__main__':
    unittest.main()
