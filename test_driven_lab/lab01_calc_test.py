import unittest
from lab01_calc_code import *


class TestCalc(unittest.TestCase):
    def test_calculator_add_method_returns_correct_result(self):
        result = calculate_add(2, 2)
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
