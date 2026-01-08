# ----------------------------------------------
# indentation use 4 spaces per indentation level
# good
x = 0
def example_function():
    if x > 0:
        print("positive number")
    else:
        print("negative number")

# ----------------------------------------------
# whitespace in expressions and statements avoid extraneous whitespace
# good
spam(ham[1],{eggs: 2})

# ----------------------------------------------
# import should usually be on separate lines and should be gropued
# good
import os
import sys
from subprocess import Popen, PIPE

# ----------------------------------------------
# comments write comments sparingly and keep them concise. let the code speak for otself whenever possible
# good
x = x + 1 # increment x

# ----------------------------------------------
# descriptive variable and function names: choose names that reflect the porpode of variables and functions
# good

total_student = 100
def calculate_average(scores):
    # calculate the average of alist of scores
    return sum(scores) / len(scores)

print(calculate_average([1, 2, 3, 4, 5]))

# ----------------------------------------------
# avoiding magic numbers and string replace magic numbers and string with constants
# good
max_score = 100
pass_threshold = 60

if student_score > pass_threshold:
    print("pass!")

# list and dictionary use comprehension for concise and expressive creation of list and dicts
# good
square = [x**2 for x in range(10)]
square_dict = {x: x**2 for x in range(10)}

# avoiding global variables minimize the use of global variables and prefer passing parameters to functions
def calculate_area(radius):
    pi = 3.14
    return pi * radius ** 2