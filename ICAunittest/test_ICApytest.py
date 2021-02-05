import pytest
from ICAunittest import *

calculator = Calculator()

class TestCase:
    
    def test_1(self):
        assert calculator.addition(2, 5) == 7

    def test_2(self):
        assert calculator.addition(-2, 1) == -1

    def test_3(self):
        assert calculator.subtraction(6, 3) == 3

    def test_4(self):
        assert calculator.multiplication(2, 5) == 10

    def test_5(self):
        assert calculator.division(2, 0) == "ZeroDivisionError"


