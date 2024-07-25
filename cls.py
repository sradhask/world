class House:
    squarefeet=1500
    color="white"
    cost=2000000
    def hlo(self,k):
        print("New Home",k)
        print("squarefeet")
        print(self.squarefeet)
        
p=House()
p.hlo("for sale")