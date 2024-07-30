class Car:
    def main(self):
        print("move")
class Bike(Car):
     def main(self):
         print("ride")
p1=Car()
p2=Bike()
p1.main()
p2.main()