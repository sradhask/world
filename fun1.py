class A:
     def mainfun(self):
        print("hello")
class B(A):
     def mainfun2(self):
          print("hai")
p1=A()
p2=B()
p1.mainfun()
p2.mainfun2()
p2.mainfun()