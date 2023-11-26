class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self, interest_rate):
        interest = self.balance * (interest_rate / 100)
        self.deposit(interest)
        print(f"Interest added: ${interest} (at {interest_rate}% rate)") # adauga mereu la balanta curenta 5%

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit")

if __name__ == "__main__":
    savings = SavingsAccount("Robert's account", 1000)
    checking = CheckingAccount("Rooney's account", 500)

    savings.deposit(500)
    savings.calculate_interest(5)   # aici adauga 5%, adica 75

    checking.withdraw(200)
    checking.withdraw(800)
