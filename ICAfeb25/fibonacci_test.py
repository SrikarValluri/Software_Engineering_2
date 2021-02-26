import unittest
import pytest
from fibonacci import fibonacci

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci(1), 1)
    
    def test2(self):
        self.assertEqual(fibonacci(4), 3)

    def test4(self):
        self.assertEqual(fibonacci(-1), "Invalid Input.")

    def test4(self):
        self.assertEqual(fibonacci("bruh"), "Invalid Input.")  


class TestCase2:
    
    def test_1(self):
        assert fibonacci(1) == 1

    def test_2(self):
        assert fibonacci(4) == 3

    def test_3(self):
        assert fibonacci(-1) == "Invalid Input."

    def test_4(self):
        assert fibonacci("bruh") == "Invalid Input."



if __name__ == "__main__":
    unittest.main()
