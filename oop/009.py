#814

class Bank:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"I deposit to your account:\n{amount}")
        self.print_balance()

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"I withdraw from your bank account:\n{amount}")
        else:
            print("Error: not enough money")
        self.print_balance()

    def print_balance(self):
        print(f"On the account: {self.__balance:.2f}")

# Створення об'єктів класу Bank
account1 = Bank(0)
account2 = Bank(0)

# Покладання коштів на рахунок та зняття з рахунку
account1.deposit(5000)
account1.withdraw(4200)

account2.deposit(1000)
account2.withdraw(1200)
