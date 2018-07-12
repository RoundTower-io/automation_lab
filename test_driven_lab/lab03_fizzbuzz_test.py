import unittest
from lab03_fizzbuzz_code import *


class TestFizzBuzz(unittest.TestCase):
    def test_if_value_return_is_fizz(self):
        result = fizzbuzz(33)
        self.assertEqual('Fizz', result)

    def test_if_value_return_is_buzz(self):
        result = fizzbuzz(50)
        self.assertEqual('Buzz', result)

    def test_if_value_return_is_fizzbuzz(self):
        result = fizzbuzz(30)
        self.assertEqual('FizzBuzz', result)

    def test_if_value_return_is_number(self):
        result = fizzbuzz(4)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
