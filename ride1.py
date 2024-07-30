class hi:
    def hlo(self):
        print("hello")

class world(hi):
    def hlo(self):
        print("nature")
class sky(world):
    def hlo(self):
        print("stars")

 
p1=hi()
p2=world()
p3=sky()
p1.hlo()
p2.hlo()
p3.hlo()