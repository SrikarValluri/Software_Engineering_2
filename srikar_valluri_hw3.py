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
    while(True):
        year = str(input("Enter input year: "))
        try:
            year = int(year)
            if(year > 0):
                output = is_leap_year(year)
                if(output == True):
                    print(str(year) + " is a leap year.")
                else:
                    print(str(year) + " isn't a leap year.")
                break;
            else:
                print(str(year) + " is not a valid year.")
        except:
            print("You have not entered a valid integer.\n")
            
main()
