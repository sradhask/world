print ("""1.addition
        2.substaction
        3.multiplication
        4.division
     enter your choice""")
choice=int(input())
a=int(input("enter a number"))
b=int(input("enter a number"))

if choice==1:
  x=lambda a,b:a+b
  print(x(a,b))
if choice==2:
  x=lambda a,b:a-b
  print(x(a,b))
if choice==3:
  x=lambda a,b:a*b
  print(x(a,b))
if choice==4:
  x=lambda a,b:a/b
  print(x(a,b))
else:
  print("enter your choice")