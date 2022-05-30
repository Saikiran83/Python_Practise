import sys
class banking:
    "banking operations"
    bank_name = 'SAI BANK'
    def __init__(self,name,balance = 0.0):
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        self.balance = self.balance + amt 
        print("balance after deposit is:",self.balance)
    def withdraw(self,amt):
        if amt > self.balance :
            print("insufficient funds")
            sys.exit()
        self.balance = self.balance - amt 
        print("balance after withdrawal is:",self.balance )
print("welcome to ", banking.bank_name)
name = input("enter name:")
c = banking(name)
while True:
    print('d-Deposit \nw-Withdraw \ne-exit') 
    option = input("enter option:")
    if option == 'd':
        amt = float(input("enter amount:"))
        c.deposit(amt)
    elif option == 'w':
        amt = float(input("enter amount"))
        c.withdraw(amt)
    elif option == 'e':
        print("wrong option")
        sys.exit()
    else:
        print("thanks for banking")

     
