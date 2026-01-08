from abc import ABC, abstractmethod

# In the world of software engineering, design patterns are recurring solutions
# to common problems. These patterns provide a template for solving issues
# in a way that promotes code reuse, maintainability, and flexibility

"""
Singleton Pattern: Ensuring a Class has Only One Instance
The Singleton pattern is a creational design pattern that ensures a class has
only one instance and provides a global point of access to it. This can be
useful in scenarios where exactly one object is needed to coordinate actions
across the system.
"""
"""
class Log:
    def __init__(self):
        self.logs = []

    def add_log(self, log):
        self.logs.append(log)
        return print(f"Added log: {log}")

log1 = Log()
log2 = Log()
print(log1 is log2)
log1.add_log("python is awsome")
log2.add_log("hello world")
print(log2.logs)
"""
# singleton
class Log:
    logs : list[str] = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def add_log(self, log):
        self.logs.append(log)
        return print(f"Added log: {log}")

log1 = Log()
log2 = Log()
print(log1 is log2)
log1.add_log("python is awsome")
log2.add_log("hello world")
print(log2.logs)

"""
Factory Pattern: Creating Objects
The Factory pattern is another creational design pattern that provides an
interface for creating objects but allows subclasses to alter the type of
objects that will be created. It promotes loose coupling by abstracting the
instantiation process, making the system more scalable. Let's explore the
Factory pattern through a simple example:
"""
class Product(ABC):
    @abstractmethod
    def display(self):
        pass

class ConcreteProductA(Product):
    def display(self):
        print("Product A")

class ConcreteProductB(Product):
    def display(self):
        print("Product B")

class ProductFactory:
    def create_product(self, product_type):
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()

factory = ProductFactory()
product_a = factory.create_product("A")
product_b = factory.create_product("B")

product_a.display()
product_b.display()

"""
Decorator Pattern: Extending Class Behavior
The Decorator pattern is a structural design pattern that allows behavior to
be added to an individual object, either statically or dynamically, without
affecting the behavior of other objects from the same class. It is often used
to extend or alter the functionality of objects at runtime. Let's implement the
Decorator pattern:
"""

class Component:
    def operation(self):
        pass
class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"
class Decorator(Component):
    _component = None

    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(component)
decorator_b = ConcreteDecoratorB(decorator_a)
print(decorator_b.operation())  # Output:








