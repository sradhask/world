print("""1.addition
        2. Substraction
        3.division 
        4.multiplication
         enter your choice """)
choice=int(input())
a=int(input("enter a number"))
b=int(input("enter a number"))
if choice==1:
    sum=a+b
    print("the sum is ",sum)
elif choice==2:
    substraction=a-b
    print("the  difference is",difference)
elif choice==3:
    division=a/b
    print("the division is ",division)
elif choice==4:
    multiplication=a*b
    print("the multiplication is",multiplication)
else:
    print("wrong choice")
        