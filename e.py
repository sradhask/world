print("""1.Addition
    2.substraction
    3.division
    4.multiplication
      enter your choice"""  )
choice=int(input()) 
a=int(input("enter a number"))
b=int(input("enter a number")) 
if choice==1:
   sum=a+b
   print("the sum is,",sum)
elif choice==2:
   difference=a-b
   print("the difference is",difference)
elif choice==3:
   product=a*b
   print("the product is",product)
elif choice==4:
   quotient=a/b
   print("the quotient is",quotient)
else:
   print("wrong  choice")

   