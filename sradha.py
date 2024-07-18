a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
        print("invalid")
