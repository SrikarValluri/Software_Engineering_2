def fibonacci(x):
    try:
        if(x == 0):
            return 0;
        elif(x == 1):
            return 1
        elif(x < 0):
            return "Invalid Input."
        else:
            return fibonacci(x-1) + fibonacci(x-2)
    except:
        return "Invalid Input."

def factorial(x):
    try:
        if(x == 0):
            return 1;
        elif(x == 1):
            return 1
        elif(x < 0):
            return "Invalid Input."
        else:
            return x * factorial(x-1)
    except:
        return "Invalid Input."