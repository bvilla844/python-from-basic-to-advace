# As ordered and mutable sequences, lists provide flexibility for storing and
# manipulating data. Let's explore their key characteristics:
#     Ordered Sequence: Lists maintain the order in which elements are
#                       added, allowing for easy indexing and retrieval.
#     Mutable Nature: The ability to modify, add, or remove elements
#                       makes lists a powerful choice for dynamic d

fruits: list = ["apple", "banana", "cherry"]

# accessing
print(fruits[2])

# modifying
fruits[1]="coconut"
print(fruits)

# adding
fruits.append("orange")
print(fruits)

#removing
fruits.remove("apple")
print(fruits)

print(type(fruits))

#indexing
subset = fruits[0:2]
print(subset)

#order
numbers = [5, 23, 3, 67, 100 ]
numbers_str = ["5", "23", "3", "67", "100" ]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
sorted_numbers_len = sorted(numbers_str, key=len)
print(sorted_numbers_len)

# reverse
numbers = [5, 23, 3, 67, 100 ]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers)

# concatenation
new_list  = numbers + reversed_numbers
print(new_list)

# operations
new_list_mult = new_list * 5
print(new_list_mult)

# counting and occurrences
fruits: list = ["apple", "banana", "cherry", "apple", "banana",]
print("apple" in fruits) # true
print(fruits.count("apple")) # 2
print(len(fruits)) # 5

data_list = [4, 6, 65, 43, 2, 1, 22, 11]
data_tuple = tuple(data_list)
data_set = set(data_list)

sorted_data_list = sorted(data_set)
sorted_data_tuple = tuple(sorted(data_tuple))
sorted_data_set = sorted(data_set)

print(sorted_data_list)
print(sorted_data_tuple)
print(sorted_data_set)