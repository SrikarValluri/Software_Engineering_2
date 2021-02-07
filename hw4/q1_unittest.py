import unittest
from q1 import cube

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube(3), 27)
    
    def test2(self):
        self.assertEqual(cube(-6.7), -6.7 * -6.7 * -6.7)
    
    def test3(self):
        self.assertEqual(cube("bruh"), "Invalid Input. Not a number.")  


if __name__ == "__main__":
    unittest.main()