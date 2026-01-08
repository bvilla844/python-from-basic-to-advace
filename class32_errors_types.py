# error types

# SyntaxError
# print "hola mundo" # Error
print("hola mundo")

# NameError
# print(language) # Error
language = "Python"
print(language)

# IndexError
my_list = ["Python", "Javascript", "Php"]
# print(my_list[4]) # Error
print(my_list[2])

# ModuleNotFound
# import maths # Error
import math

# AttributeError
# print(math.PI) # Error
print(math.pi)

# KeyError
person : dict = {
    "name" : "josep",
    "age" : 22,
    "occupation" : "engineer",
    "address" : {
        "city":"new york",
        "state":"ny",
        "country":"USA"
    }
}
# print(person["income"]) # Error
print(person["name"])

# TypeError
x = 5
y = "20"
# print(x + y) # Error

# ImportError
# from math import PI # Error
from math import pi

# ValueError
# my_int = int("20 anos") # Error
my_int = int("20")
print(my_int + 10)
