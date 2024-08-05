class bank():
    def __int_(self,accountnum,balance):
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
       
    