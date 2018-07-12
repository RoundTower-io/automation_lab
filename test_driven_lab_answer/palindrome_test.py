# A palindrome is a word, phrase, or sequence that reads the same backward as forward.
# For example, the word mom and the number 4334 are palindromes
# Instructions:
# Write test cases that check the function does the following:
#  - Pass true if the passed string is a palindrome
#  - Pass false if the passed string is not a palindrome
#  - Is case insensitive
#  - The function  parses numbers in addition to string
import unittest
from palindrome_code import *


class TestPalindrome(unittest.TestCase):
    def test_if_value_is_a_palindrome(self):
        result = palindrome_check('mom')
        self.assertEqual(True, result)

    def test_if_value_is_not_a_palindrome(self):
        result = palindrome_check('hello')
        self.assertEqual(False, result)

    def test_if_value_is_not_string(self):
        result = palindrome_check(4334)
        self.assertEqual(True, result)

    def test_if_value_is_capitalized(self):
        result = palindrome_check('Mom')
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
