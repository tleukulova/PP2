""""
class Account:
    def __init__(self,name,m):
        self.name=name
        self.m=m
    def Deposit(self,a):
        self.m+=a
    def Withdraw(self,a):
        if a > self.m:
           print("STOP!")
        else:
            self.m-=a
name_account=input()
m_account=float(input())
account=Account(name_account,m_account)
a_account=float(input())
account.Deposit(a_account)
a_account=float(input())
account.Withdraw(a_account)
"""



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")

# Instantiate the BankAccount object
account = BankAccount("Tleukulova Aruzhan", 1000)

# Make deposits and withdrawals
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)  # Should print "Insufficient funds."
account.deposit(-100)   # Should print "Deposit amount must be greater than zero."

