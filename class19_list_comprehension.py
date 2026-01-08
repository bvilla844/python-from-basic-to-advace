# List comprehensions provide a concise syntax for creating lists in a single
# line of code. The basic structure consists of an expression followed by a
# for clause, which is then followed by zero or more if clauses. This
# structure allows for the creation of lists by applying an expression to each
# item in an iterable, optionally filtering the items based on specified
# conditions

# In some cases, list comprehensions can offer performance benefits over
# traditional loops. The concise nature of list comprehensions often translates
# to faster execution times.

# traditional
numbers = []
for x in range(10):
    numbers.append(x)

print(numbers)

# list comprehension
number_list = [x for x in range(10)]
print(number_list)

celsius_temp = [10, 20, 30, 40, 50]
fahrenheit_temp = [(9 / 5) * temp + 32 for temp in celsius_temp]
print(celsius_temp)
print(fahrenheit_temp)

# conditional in list comprehension
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

# nesting in list comprehension
numbers_list = [[1, 2, 3], [4, 5, 6,], [7, 8, 8]]
flattened_numbers = [num for row in numbers_list for num in row ]
print(flattened_numbers)

# sales data
product_sales = {
    ("product A","january"): 150,
    ("product B","january"): 350,
    ("product C","january"): 100,
}

total_sales_per_product = {
    product: sum(
        sales
        for (p, m), sales in product_sales.items()
        if p == product
    )
    for product in unique_products
}
