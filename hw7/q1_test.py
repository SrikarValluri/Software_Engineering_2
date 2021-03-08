import unittest
from q1 import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz(1), "1")

if __name__ == "__main__":
    unittest.main()