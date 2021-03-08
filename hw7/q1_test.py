import unittest
from q1 import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz(1), "1")
    def test2(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
    def test3(self):
        self.assertEqual(fizzbuzz(5), "Buzz")        

if __name__ == "__main__":
    unittest.main()