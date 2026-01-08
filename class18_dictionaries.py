# Dictionaries, often referred to as dicts, are an integral part of Python's data
# structures. Unlike sequences such as lists and tuples that use indices for
# access, dictionaries use keys for retrieval. This key-value pairing allows for
# efficient data organization and retrieval.

person : dict = {
    "name" : "josep",
    "age" : 22,
    "occupation" : "engineer"
}
print(person)

# accessing values
print(person["name"]) # output josep
print(person["age"]) # output 22

# modifying values
person["name"] = "daniel"
print(person)

# adding item
person["location"] = "new york"
print(person)

# deleting item
del person["occupation"]
print(person)

# nesting dict
person : dict = {
    "name" : "josep",
    "age" : 22,
    "occupation" : "engineer",
    "address" : {
        "city":"new york",
        "state":"ny",
        "country":"USA"
    }
}
print(person["address"]["state"])
print(type(person))

students = [
    {
        "name": "josep",
        "age": 22,
    },
    {
        "name": "victor",
        "age": 30,
    },
    {
        "name": "alice",
        "age": 44,
    }
]

sorted_students = sorted(students, key= lambda x : x["name"])
print(sorted_students)