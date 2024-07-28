num1=int(input("enter a number"))
a=0
b=num1
while(num1>0):
 r=num1%10
 a=a*10+r
 num1=num1/10
 print(a)
 if (b==a):
     print("the given number is palindrome")
else:
    print("the given number is not pallindrome")