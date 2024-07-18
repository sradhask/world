
print("enter the marks")
d=[]
for i in range(5):
    a=int(input())
    d.append(a)

c=sum(d)
try:
    
    if sum<=25:
        raise TypeError
    
except ValueError:
    print("passed")
else:
    print("passed")