from abc import  ABC,abstractmethod
class vehicle(ABC):
  @abstractmethod
  def move(self):
    print("moving vehicle")
class car(vehicle):
  def move(self):
    print("moving car")
class bike (vehicle):
  def move(self):
    print("moving bike")
p2=car()
p3=bike()
p2.move()
p3.move()
  