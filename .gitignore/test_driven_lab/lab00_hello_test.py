import unittest
from lab00_hello_code import *

class testhello(unittest.TestCase): 
    def test_if_hello_is_returned(self):
        result = helloWorld()
        self.assertEqual('Hello!', result)

if __name__ == '__main__':
    unittest.main()