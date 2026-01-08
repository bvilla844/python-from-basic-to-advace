# Inheritance is a fundamental concept in OOP that allows a new class,
# known as the subclass or derived class, to inherit attributes and methods
# from an existing class, referred to as the superclass or base class. This
# concept promotes code reuse, as it enables the creation of specialized
# classes based on existing, more general ones.

"""
The power of inheritance becomes evident when a subclass has the ability
to override methods inherited from the superclass. This allows for
customization and specialization of behavior, tailoring it to the specific
needs of the subclass.
"""

class Animal:
    def speak_func(self):
        print("animals spek")

class Dog(Animal):
    def woof_func(self):
        print("dog woof")

dog = Dog()
dog.speak_func()

class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        return area
my_square = Square(5,5)
print(my_square.area())

# Polymorphism, a core OOP concept, allows objects of different classes to
# be treated as objects of a common base class. Method overriding is a key
# mechanism in achieving polymorphism, as it enables different classes to
# provide their own implementations of methods with the same name.

class Bird:
    def make_sound(self):
        print("Bird makes sound")

class Chicken(Bird):
    def make_sound(self):
        print("Chicken makes piopio")

class Hawk(Bird):
    def make_sound(self):
        print("Hawk makes awwww")

chicken = Chicken()
chicken.make_sound()

hawk = Hawk()
hawk.make_sound()

