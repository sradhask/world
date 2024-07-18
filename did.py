try:
    a=int(input("enter a number"))
except:
    print("enter only numbers")
else:
    print("the number is ",a)
finally:
    print("completed")