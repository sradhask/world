a=int(input("enter the number"))
b=[]
for i in a:
     print(a[i])
     if [i]%2==0:
      b.append(i)    
      b=tuple(b)
      print(b)
          
