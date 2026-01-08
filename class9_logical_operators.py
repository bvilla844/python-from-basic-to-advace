# Logical operators allow you to combine and manipulate boolean values to
# make more complex decisions.
# and : Returns True if both conditions are true.
# or : Returns True if at least one condition is true.
# not : Returns the opposite boolean value.

x = True
y = False

result_and = x and y
result_or = x or y
result_not = not x

print(result_and, result_or, result_not)

age = 25
income = 350
is_student = True
if age >= 18 and (income > 500 or is_student):
    print("you qualified for a loan")
else:
    print("you do not qualify for a loan")