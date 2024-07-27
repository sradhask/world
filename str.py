class hlo():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name} {self.age}"
p=hlo("john",25)
print(p)