a=input("enter a name")
import re
x=re.findall("$p",a)
if x:
    print("it ends with p",a)
else:
    print("it does ends with p",a)