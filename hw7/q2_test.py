import unittest
from q2 import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear(2000), "True")

if __name__ == "__main__":
    unittest.main()