# """
# Create a class BankAccount with attributes name and balance.

# Add methods deposit(amount) and withdraw(amount) that update the balance and showbalance().

# Prevent withdrawal if the balance is less than the amount and print a warning message.
# Create two BankAccount objects and try deposit and withdraw money from the account

# Bonus: simulate a transfer(amount, to_account) method to transfer between two bank accounts
# """


class BankAccount:
    # constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # methods
    def deposit(self, amount):
        self.balance =  self.balance+ amount 
        print(f"amount deposited to {self.name}!")
        print(f"Current Balance of {self.name} is {self.balance}")

    def transfer_to(self, amt, to_account):
        # my account withdraw
        self.withdrawal(amt)
        # sending money to another account
        to_account.deposit(amt)

    def showbalance(self):
        print(self.balance)

    def withdrawal(self, amount):
        if self.balance < amount:
            print("insufficient balance ")
        else:
            self.balance -= amount
            print(f"amount withdrawn = {amount} by {self.name}!")
            print(f"Current Balance of {self.name} is {self.balance}")


my_acc = BankAccount("john", 10000)

# recipient
niroshini_acc = BankAccount("NA", 1000)

# transfer
my_acc.transfer_to(500, niroshini_acc)

# # Question 2


# parent
class Factory:
    def __init__(self):
        pass

    def make_vehicle(self):
        print("I am making a general vehicle")


# class Child_class_name(Parent_Class_name)
class CarFactory(Factory):
    def __init__(self):
        pass

    # manufacturing cars
    def make_cars(self):
        print("I am manufacturing only CARS")

    def make_vehicle(self):
        print("I am changing my grandparent class to my own")


class BikeFactory(Factory):
    def __init__(self):
        pass

    def make_bikes(self):
        print("I am manufacturing only bikes")

    def make_vehicle(self):
        print("I am changing my grandparent class to my own")


new_car_factory = CarFactory()
# self property
new_car_factory.make_cars()
# parent property
new_car_factory.make_vehicle()






