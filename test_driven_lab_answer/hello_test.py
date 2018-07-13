import unittest
from hello_code import *


class TestHello(unittest.TestCase):
    def test_if_hello_is_returned(self):
        result = hello_world()
        self.assertEqual('Hello!', result)


if __name__ == '__main__':
    unittest.main()
