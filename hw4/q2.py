def avgList(x):
    try:
        return sum(x)/len(x)
    except ZeroDivisionError:
        return "No Values In The List."
    except:
        return "Invalid Data Type."