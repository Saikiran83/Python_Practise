import sys
class banking:
    "bank operations"
    bank_name = 'SAI BANK'
    def __init__(self,name,balance = 0.0):
        self.name = name 
        self.balance = balance 
    def deposit(self,amount):
        self.balance = self.balance + amount 
        print("balance after deposit is:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds")
            sys.exit()
        self.balance = self.balance - amount 
        print("balance after withdraw:",self.balance)
print("welcome to ",banking.bank_name)
name = input("enter your name:")
c = banking(name)
while True:
    print('d-Deposit \nw-Withdraw \ne-exit')
    option=input('Choose your option:')
    if option == 'd' or option == 'D':
        amount = float(input("enter amount:"))
        c.deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input("enter amount:"))
        c.withdraw(amount)
    elif option == 'e' or option == ' E':
        print("thanks for banking")
        sys.exit
    else:
        print("invalid option, choose correct option")




    

     