# Functions, in the programming paradigm, encapsulate a set of instructions
# that can be executed with a single call.

# Think of functions as building blocks, each designed
# for a specific purpose, contributing to the overall structure of your code
def calculate_avg(num1, num2, num3):
    pass

def greeting(name):
    return print(f"hello {name}")

greeting("andres")

# Calling a function involves providing values, known as arguments, for its
# parameters. Python supports various ways to pass arguments,

# What are Parameters? In the context of a function, parameters act as placeholders for values that
# the function expects to receive when it is called.

# positional argument
result = calculate_avg(10,20,30)

# keyword argument
result = calculate_avg(num1 = 10, num2 = 20, num3=30)

# mix combination
result = calculate_avg(10, num2 = 20, num3=30)


def calculate_area_recta(shape, **parameters):
    if shape == "square":
        return parameters["width"] * parameters["height"]
    elif shape == "rectangle":
        return (parameters["width"] * parameters["height"])/2
    elif shape == "circle":
        return 3.1416 * parameters["radius"] **2
    else:
        return "no valid shape"


square_area = calculate_area_recta(shape = "square", width = 100, height = 100)
print(square_area)

# The *args syntax in a function definition allows it to accept a variable
# number of positional arguments.

def receiving_args(*args):
    for arg in args:
        print(arg)

receiving_args(1,2,3,4,5)


# Similarly, the **kwargs syntax collects variable keyword arguments into a
# dictionary.

def receiving_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

receiving_kwargs(name = "john", age = 20, city = "New York")