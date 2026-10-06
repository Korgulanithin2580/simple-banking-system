class Account:

    def __init__(self, account_number, name, password, balance=0):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount

    def check_balance(self):
        return self.balance