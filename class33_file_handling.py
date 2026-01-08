# File handling is a crucial aspect of programming that involves the
# manipulation of data stored in files. Understanding how to read from and
# write to files is fundamental to many real-world applications, ranging from
# data analysis to configuration management.

import os
#     Text Files:
#     •Definition: Plain text files contain human-readable text and are the simplest form of file storage.
#     •Applications: Configuration files, logs, source code files.

# read
with open("my_file.txt") as file:
    content = file.read()
    # print(content)

    for line in file:
        print(line)
    file.close()

txt_file = open("my_file.txt", "r+") # leer y escribir
txt_file.write("mi nombre es andre\ntengo 27 anos\nme gusta python")
# print(txt_file.read())
# print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

# write
txt_file.write("\nme gusta disenar soluciones tecnologicas")
txt_file.close()

#     JSON Files:
#     •Definition: JavaScript Object Notation files store data in a humanreadable format with key-value pairs.
#     •Applications: Configuration files, web APIs, data interchange between languages.
import json
json_file = open("my_file.json", "w+") # leer y escribir

json_test = {
    "name" : "josep",
    "age" : 22,
    "occupation" : "engineer"
}

json.dump(json_test, json_file, indent=2)

for line in json_file.readlines():
    print(line)

#     CSV Files:
# •    Definition: Comma-Separated Values files store tabular data, where
# each line represents a record, and values are separated by commas.
# •    Applications: Data exchange between spreadsheet software, database
# exports.
