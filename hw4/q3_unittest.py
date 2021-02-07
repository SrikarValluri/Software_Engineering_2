import unittest
from q3 import firstLast

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(firstLast("Srikar", "Valluri"), "Srikar Valluri")
    
    def test2(self):
        self.assertEqual(firstLast("Bruh", "Moment"), "Bruh Moment")
    
    def test3(self):
        self.assertEqual(firstLast("John", "Doe"), "John Doe")  


if __name__ == "__main__":
    unittest.main()