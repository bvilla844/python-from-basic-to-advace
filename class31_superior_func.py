# functions that incorporates the system


# CLOSURE
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add


print((sum_ten(10))(5))

# Map
numbers = [2, 30, 55, 5, 6, 8, 10]
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# filter
def filter_greater_ten(number):
    if number > 10:
        return True
    return False
print(list(filter(filter_greater_ten, numbers)))

# reduce
def sum_two_values(first_value, second_value):
    print(first_value, second_value)
    return first_value + second_value
print(reduce(sum_two_values, numbers))