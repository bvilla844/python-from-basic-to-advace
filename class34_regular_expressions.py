# regular expressions

# match
import re
my_str = "esta es la leccion 7 leccion de expressiones regulares"
match = re.match("esta es la le", my_str)
print(match.span())
print(match.group())

# search
search = re.search("leccion", my_str)
print(search.span())
print(search.group())

# findall
findall = re.findall("leccion", my_str)
print(findall)

# split
print(re.split("leccion", my_str))

# sub
print(re.sub("leccion", "LECCION", my_str))