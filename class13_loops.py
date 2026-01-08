# Loops are a powerful mechanism for automating repetitive tasks

# The for loop in Python is particularly useful when you want to iterate over
# a sequence of elements. This sequence can be a list, tuple, string, or any
# other iterable object.

fruits = ["apple", "banana", 'orange']
for fruit in fruits:
    print(fruit)

message = "hello world"
for letter in message:
    print(letter)

# While the for loop is ideal for iterating over known sequences, the while
# loop is employed when the number of iterations is unknown, and the loop
# continues as long as a certain condition is true.

counter = 1
while counter < 11:
    print(counter)
    counter += 1

# Python provides two essential loop control statements, break and continue , each serving a
# distinct purpose.

# break
for number in range(10):
    print(number)
    if number == 5:
        print("condition met")
        break

# continue
for number in range(10):
    if number % 2 == 0:
        print(f"{number} is even number")
    elif number % 2 == 1:
        continue

word = "hello everyone"
vowels = "aeiou"

for letter in word:
    if letter in vowels:
        continue
    else:
        print(letter)