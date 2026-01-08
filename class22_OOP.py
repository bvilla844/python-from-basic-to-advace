"""
Object-Oriented Programming (OOP) is a paradigm that organizes code
around the concept of objects, encapsulating data and behavior within them.
In OOP, software is modeled as a collection of interacting objects, each
representing an instance of a class. A class serves as a blueprint for creating
objects, defining their properties (attributes) and actions (methods).
The significance of OOP lies in its ability to provide a modular and
structured approach to software development. By breaking down complex
systems into manageable objects, OOP promotes code reuse,
maintainability, and scalability. This section delves into the fundamental
principles of OOP that contribute to its significance in modern
programming.

"""
"""
The core principles of OOP—encapsulation, inheritance, and polymorphism
—are the pillars on which the paradigm stands. Each principle addresses
specific aspects of code organization and functionality.
•    Encapsulation: Encapsulation involves bundling data (attributes) and
methods that operate on the data into a single unit, i.e., an object. This
promotes data hiding, limiting access to an object's internal details. The
section demonstrates how encapsulation enhances code security and
modularity.
•    Inheritance: Inheritance allows a new class (subclass) to inherit
properties and methods from an existing class (superclass). This
mechanism supports code reuse and the creation of specialized classes
based on existing ones. Real-world examples illustrate how inheritance
facilitates the modeling of relationships between objects.
•    Polymorphism: Polymorphism enables objects of different types to be
treated as objects of a common base type. This flexibility simplifies
code design and promotes extensibility. The section explores examples
of polymorphism through method overloading and overriding.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def spark(self):
        print(f"{self.name} does woof")

dog = Dog("Pep", 20)
dog.spark()

