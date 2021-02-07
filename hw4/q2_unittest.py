import unittest
from q2 import avgList

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(avgList([0, 7, 3, 10, 6, 10]), 6)
    
    def test2(self):
        self.assertEqual(avgList([]), "No Values In The List.")
    
    def test3(self):
        self.assertEqual(avgList("bruh"), "Invalid Data Type.")  


if __name__ == "__main__":
    unittest.main()