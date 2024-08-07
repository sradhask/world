a=input("enter your password \n")
import re 
x=re.search("he.{2}o",a)
print(x)
if x:
     print("the password contains 8 characters")
else:
    print("invalid password")
            