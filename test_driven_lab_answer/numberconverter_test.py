# Instructions:
# Create a function
#  - That accepts a list of integers as an input
#  - Then returns a list that contains each number spelled out
#
# For example
#  - The list [1,23,6,66,10]
#  - Would be returned as [one, twothree, six, sixsix, onezero]

# Create tests for the code that you believe would best fit for this function.
import unittest
from numberconverter_code import *


class Testnumbers_to_names(unittest.TestCase):
    def test_if_list_converted(self):
        result = numbers_to_names([2, 3, 44, 23, 1])
        self.assertEqual(['two', 'three', 'fourfour', 'twothree', 'one'], result)

    def test_if_list_converted_tripple_digits(self):
        result = numbers_to_names([2, 3, 449, 23, 1110])
        self.assertEqual(['two', 'three', 'fourfournine', 'twothree', 'oneoneonezero'], result)


if __name__ == '__main__':
    unittest.main()
