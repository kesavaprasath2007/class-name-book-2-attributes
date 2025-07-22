class Bankaccount():
     def __init__(self,name,balance):
       
          self.name=name
          self.balance=balance

     def deposit(self,amount):
        self.balance+= amount
        print("Deposited:",amount)

     def withdraw(self,amount): 
        if amount<=self.balance:
            self.balance-=amount
            print("withdrawn:",amount)
        else:
           print("insufficient balance")
     def check_balance(self):
        
        print("balance:",self.balance)
        
name=input("Enter your name:")
balance=int(input("Enter your starting balance:"))
deposit=int(input("Enter your deposit amount:"))
withdraw=int(input("Enter your withdraw amount:"))
a=Bankaccount(name,balance)
a.deposit(deposit)
a.withdraw(withdraw)
a.check_balance()
    
