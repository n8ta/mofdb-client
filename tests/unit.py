import unittest
from mofdb.main import add_one

class BasicTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(add_one(1), 2)  # add assertion here

if __name__ == '__main__':
    unittest.main()
