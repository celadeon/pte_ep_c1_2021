class BankAccount:
    def __init__(self, name: str, account_number: int, balance: int):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def __str__balance(self):
        return "balance: {}".format(self.balance)

    def withdraw(self, amount: int):
        self.balance -= amount

    def deposit(self, amount: int):
        self.balance += amount