def is_leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def main():
    year = int(input("Enter input year: "))
    output = is_leap_year(year)
    if(output == True):
        print(str(year) + " is a leap year.")
    else:
        print(str(year) + " isn't a leap year.")
        

main()
