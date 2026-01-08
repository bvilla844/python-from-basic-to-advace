# Integers represent whole numbers without any decimal point
age = 25
print(age + 5, "-> data type: ", type(age))

# Floats, or floating-point numbers, include decimal points and allow for
# more precision in numerical operations.
price = 19.99
discount = 0.99
total_price = price * discount
print(total_price, "-> data type: ", type(total_price))

# Strings represent sequences of characters. They are versatile and used for
# representing text in Python.
name = "John"
greeting = "hello, how are you?"
message = greeting + " " + name
print(message, "-> data type: ", type(message))

# Booleans represent truth values, either True or False . They are
# fundamental for decision-making in programming.
is_adult = True
is_student = True
can_vote = is_adult and not is_student
print(can_vote, "-> data type: ", type(can_vote))