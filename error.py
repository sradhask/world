a=int(input("enter the elements"))
print("enter the numbers")
d=[]
for i in range (a):
    b=int(input())
    d.append(b)
try:
    c=sum(d)/a
except ZeroDivisionError:
    print("enter atleast two numbers")       



