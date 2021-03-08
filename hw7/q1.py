def fizzbuzz(x):
    if(x % 3 == 0):
        print("Fizz")
        return("Fizz")
    elif(x % 5 == 0):
        print("Buzz")
        return("Buzz")
    else:
        print(x)
        return(str(x))