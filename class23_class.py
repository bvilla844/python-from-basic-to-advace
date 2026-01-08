"""
Definition of Classes and their Role in OOP
In Python, a class is a blueprint for creating objects. It defines a data
structure that encapsulates data attributes and methods that operate on those
attributes. Think of a class as a template or a prototype that specifies how
objects of that type should behave.

"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def info_car(self):
        print(f"{self.make} {self.model} {self.year}")

car = Car("Ford", "Mustang", 1999)
print(car.make)
car.info_car()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1416 * (self.radius ** 2)
my_circle = Circle(22)
print(my_circle.area())
