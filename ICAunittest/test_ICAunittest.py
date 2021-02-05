import unittest
from ICAunittest import *

calculator = Calculator()
class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.addition(2, 5), 7)
    
    def test2(self):
        self.assertEqual(calculator.addition(-2, 1), -1)
    
    def test3(self):
        self.assertEqual(calculator.subtraction(6, 3), 3)
    
    def test4(self):
        self.assertEqual(calculator.multiplication(2, 5), 10)
    
    def test5(self):
        self.assertEqual(calculator.division(2, 0), "ZeroDivisionError")  


if __name__ == "__main__":
    unittest.main()
