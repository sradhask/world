
class bank():
    def __init__(self,accountnum,balance):
       self.accountnum=accountnum
       self.balance=balance
       
    def deposit(self,account,amount):
       self.account=account
       self.amount=amount
       if(account==amount):
          print("deposit success") 
       else:
          print("deposit unsuccessed")

    def withdraw(self,account,amount):
        self.account=account
        self.amount=amount
        if(amount>=500):
           print("enter your amount")
        else:
           print("enter multiple of 100")
p1=bank()
p1.deposit()
p1.withdraw()
members={"7665":"john","3333":"herbie","8887":"susan","7786":"saf","7785":"peter"}


balance={"john":10000,"herbie":20000,"susan":800000,"saf":60000,"peter":43536}





       
    