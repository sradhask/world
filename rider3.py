class Employee:
    def __init__(self,name,salary):
      self.name=name
      self.salary=salary
    def get_status(self):
       if(100000<self.salary):
           print("High salary")
       if(50000<self.salary and 100000>self.salary):
          print("mid salary")
       if(self.salary<50000):
          print("Low salary")
    def __str__(self):
       return ("self.name-$ self.salary")
class Manager(Employee):
  def __init__(self.bonus):
     self.bo
p=Employee("sradha",50000)
print(p.name)
print(p.salary)
    
