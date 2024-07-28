class SuperClass:

    def super_method(self):
        print("Super Class method called")
        
class DerrivedClass1(SuperClass):
    def derived1_method(self):
        print("Derrived class 1 method called")

class DerrivedClass2(DerrivedClass1):

    def derived2_method(self):
        print("Derrived class 2 method called")

d2 = DerrivedClass2()

d2.super_method()  

d2.derrived1_method()  

d2.derrived2_method()  


