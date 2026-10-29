class Bankaccount:
    account_counter = 1000
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        Bankaccount.account_counter += 1
        self.account_number = Bankaccount.account_counter
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited successfully.")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif self.balance >= amount:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Error: Insufficient funds.")
    def display_balance(self):
        print("account holder:", self.account_holder)
        print("account number:", self.account_number)
        print("Current Balance:", self.balance)
    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Invalid transfer amount.")
        elif self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount

            print(amount, "transferred successfully from",
                  self.account_holder, "to",
                  other_account.account_holder)
        else:
            print("Error: Insufficient funds for transfer.")
account1 = Bankaccount("Rahul")

account1.deposit(10000)
account1.display_balance()
account1.withdraw(2000)
account1.display_balance()
