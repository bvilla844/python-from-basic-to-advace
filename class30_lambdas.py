# lambdas are anonymous functions

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(10, 20))

def sum_values(value):
    return value + sum_two_values(10, 20)

print(sum_values(10))