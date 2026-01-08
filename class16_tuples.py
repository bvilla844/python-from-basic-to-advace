# Tuples share similarities with lists but differ in their immutability. Once a
# tuple is created, its elements cannot be changed, added, or removed.
#    Ordered Sequence: Similar to lists, tuples maintain the order of elements.
#    Immutable Nature: Immutability ensures that the contents of a tuple remain constant after creation.
coordinates : tuple = (3,4)
x, y = coordinates
print(x, y) # output 3, 4

# count
my_tuple = (1,2,3,4,5,5,5)
print(my_tuple.count(5))

# index
print(my_tuple.index(5))

# union
print(coordinates + my_tuple)

#indexing
numbers = (1,2,3,4,5,6,7,8,9)
subset = numbers[1:9:2]
print(subset)

# Use cases
# Suitable for storing fixed data, such as coordinates, RGB values, etc