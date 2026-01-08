# Encapsulation involves bundling the data (attributes) and the methods that
# operate on the data into a single unit known as a class. This encapsulation
# of data and methods within a class is like placing them in a protective
# capsule. It restricts direct access to certain components, promoting a
# controlled and secure environment

# _attribute it can be used for class children but not for external code
# __attribute
class BankAccount:
    def __init__(self,account_holder, balance):
        self._account_holder = account_holder # protected
        self.__balance = balance # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        return self.__balance + amount

    def withdraw(self, amount):
        return self.__balance - amount

account = BankAccount("Andres", 100)
deposit = account.deposit(100)
print(deposit)
balance = account.get_balance()
print(balance)
withdraw = account.withdraw(500)
print(withdraw)

"""
Getters and Setters: The Gatekeepers of Encapsulation
While encapsulation restricts direct access to attributes, it provides a
controlled interface for interacting with them. Getters and setters are
methods that act as gatekeepers, allowing us to retrieve and modify attribute
values.
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter method
    def get_name(self):
        return self._name

    # setter method
    def get_age(self, new_age):
        if 0 <= new_age <= 120:
            self._age = new_age
            print(new_age)
        else:
            print("Invalid age")

person = Person("John", 40)
person_name = person.get_name()
print(person_name)
person.get_age(140)
