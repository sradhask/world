print("""1.addition
      2.substraction
      3.division
      4.multiplication
      5.enter your chice""")
choice=int(input())

if choice==1:
    def add(x,y):
      print(x+y)
    a=int(input("enter a number"))
    b=int(input("enter a number")) 
elif choice==2:
    def sub(x,y):
      print(x-y)
    a=int(input("enter a number"))
    b=int(input("enter a number"))
elif choice==3:
   def multiplication(x,y):
     print(x*y)
a=int(input("enter a number"))
b=int(input("enter a number"))
elif choice==4:
def division(x,y):
        print(x/y)
a=int(input("enter a number"))
b=int(input("enter a number"))
   
else:
print("wrong  choice")

   
    
 
