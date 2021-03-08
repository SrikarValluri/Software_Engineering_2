def leapyear(x):
    if(x % 4 == 0):
        if(x % 100 == 0):
            return("Not Leap Year")
        else:
            return("Leap Year")
    else:
        return("Not Leap Year")
