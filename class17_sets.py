# Sets are a distinct data structure in Python, offering an unordered collection
# of unique elements. Sets are particularly useful when uniqueness is a
# priority, and the order of elements doesn't matter.
#    Unordered Collection: Sets do not maintain the order of elements.
#    Unique Elements: Duplicate values

names : set = {"andres", "jose", "daniel", "andres"}
print(names)

# adding
names.add("pepe")
print(names)

# deleting
names.remove("daniel")
print(names)

# set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

print(type(names))

my_set = {"andres", "villa", 35}
print(len(my_set))
my_set.add("jose")
print(my_set)