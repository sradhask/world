a=input("enter your password")
import re 
x=re.search(["a-z A-Z],[+],[0-9]",a)
print(x)
if x:
     print("the password contains 8 characters")
else:
    print("invalid password")
            