# In Python, variables can exist in two main scopes: global and local. The
# global scope refers to the entire program, and variables declared in this
# scope are accessible from any part of the code. On the other hand, local
# scope is confined to a specific block or function, and variables declared
# within this scope are only accessible within that block or function.
from math import factorial
from functools import reduce

global_variable = 10

def global_func():
    print(global_variable)

global_func()

# Variable lifetime refers to the duration for which a variable exists in the
# computer's memory. In Python, variables have a lifetime that extends from
# the point of creation to the end of the block or function in which they are

def lifetime_func():
    local_variable = "i have a limited lifetime"
    print(local_variable)

lifetime_func()

# Global and Local variables interaction

global_var = 10
def interaction_func():
    local_var = 5
    print(f"accesing local variable: {local_var}")
    print(f"accesing global variable: {global_variable}")

interaction_func()

# nested scoop
def outer_func():
    outer_text = "this is outer text"
    print(outer_text)
    def inner_func():
        inner_text = "this is inner text"
        print(inner_text)
        print(f"calling outer text from inner text: {outer_text}")
    inner_func()

outer_func()

### advanced function concept

# recursive
def factorial_func(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_func(n - 1)
result = factorial_func(5)
print(result)

# lambda
square = lambda x: x * x
print(square(5))

# first citizen
def operator_func(operation, x, y):
    return operation(x, y)

def add_func(x, y):
    return x + y

result = operator_func(add_func,2,3)
print(result)

# decorators
def my_decorator(func):
    def wrapper():
        print("something is happening before the func is called")
        func()
        print("something is happening after the func is called")
    return wrapper

@my_decorator
def message():
    return print("hello world")

message()

# is a palindrome world

def is_palindrome(t):
    t = t.replace(" ", "").lower()
    return t == t[::-1]

print(is_palindrome("A man a plan a canal panama"))
print(is_palindrome("python"))

