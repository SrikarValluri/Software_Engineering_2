class Calculator:
    def __init__(self):
        pass

    def addition(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a-b
    
    def multiplication(self, a, b):
        return a*b
    
    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return "ZeroDivisionError"


