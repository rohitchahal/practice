try:
    n = int(input("enter neumerator"))
    d = int(input("enter denominator"))
    fraction = n/d
except ValueError:
    print("please enter correct value")
except ZeroDivisionError:
    print("please enter value other than 0")
print("finished")