#
# Instructions: Write a test to verify your dos addition function works
#
import unittest
from my_pexpect import *


class TestDosMath(unittest.TestCase):
    def test_multiplication(self):
        result = dos_multiply(3,3)
        self.assertEqual(9, result)


if __name__ == '__main__':
    unittest.main()