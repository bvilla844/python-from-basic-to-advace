# Abstract classes serve as blueprints for other classes and cannot be
# instantiated themselves. They often include abstract methods—methods
# without a defined implementation—that must be implemented by concrete
# subclasses. This enforces a contract, ensuring that specific functionalities
# are provided by subclasses

# Sirven para: Definir reglas que otras clases DEBEN cumplir y Obligar a que las clases hijas implementen ciertos métodos

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(100, 200)
print(rectangle.area())

class Walk(ABC):
    @abstractmethod
    def walk(self):
        return print("walking")

class Jump(ABC):
    @abstractmethod
    def jump(self):
        return print("jumping")

class Dog(Walk, Jump):
    def walk(self):
        print("dog walking")

    def jump(self):
        print("dog jumping")

dog = Dog()
dog.walk()
dog.jump()