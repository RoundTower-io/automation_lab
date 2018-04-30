#Instructions:
#Create a function that accepts a list of integers as an input and returns 
#a list that contains each number spelled out. If the number is longer than
#a single digit, add the converted string of each digit together. For 
#example the list [1,23,6,66,10] would be returned as
#[one,twothree,six,sixsix,onezero]

#Create tests for the code that you believe would best fit for this function.
import unittest
from numberconverter_code import *

class testconvertlist(unittest.TestCase):
    def test_if_list_converted(self):
        result = convertlist([2,3,44,23,1])
        self.assertEqual(['two', 'three', 'fourfour', 'twothree', 'one'], result)
    def test_if_list_skips_nonnumber(self):
        result = convertlist([2,3,44,'four',1])
        self.assertEqual(['two', 'three', 'fourfour', 'one'], result)
if __name__ == '__main__':
    unittest.main()