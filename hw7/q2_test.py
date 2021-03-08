import unittest
from q2 import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear(2000), "Leap Year")
    def test2(self):
        self.assertEqual(leapyear(100), "Not Leap Year") 
    def test3(self):
        self.assertEqual(leapyear(2320349), "Not Leap Year")


if __name__ == "__main__":
    unittest.main()