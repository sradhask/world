a=int(input("enter number of elements"))
print("enter the numbers")
d=[]
for i in range(a):
   c=int(input())
   d.append(c)
b=set(d)
f=[]    
for k in b:
   e=k*k
   f.append(e)

print(f)   