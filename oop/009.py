#814

class Bank:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"I deposit to your account:\n{amount}")
        self.print_balance()

    def withdraw(self, amount):
        if amount <= self.__balance + self.credit_limit:
            if self.__balance >= amount:
               self.__balance -= amount
            else:
                x = amount - self.__balance
                self.__balance = 0
                self.credit_limit -= x

            print(f"I withdraw from your bank account:\n{amount}")
        else:
            print("Error: not enough money")
        self.print_balance()
    def credit_limit(self, credit_limit):
        self.credit_limit = credit_limit
        self.print_balance()


    def print_balance(self):
        print(f"On the account own money: {self.__balance:.2f}")
        #print(f"On the account credit's money: {self.credit_limit:.2f}")
        print(self.credit_limit)


# Створення об'єктів класу Bank
account1 = Bank(0)

# Покладання коштів на рахунок та зняття з рахунку
account1.deposit(5000)

account1.credit_limit(2000)

account1.withdraw(5750)

print(account1.print_balance())
