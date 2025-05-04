import random

class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        return random.randint(1000, 9999)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.balance < amount:
            print("Insufficient balance. Withdrawal failed.")
            return False
        self.balance -= amount
        print(f"{amount} withdrawn. New balance: {self.balance}")
        return True

    def display_account_info(self):
        print(f"Account Number: {self.account_number}, Owner: {self.owner.name}, Balance: {self.balance}")
