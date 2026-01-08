# request user input
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = number1 + number2 # addition
    print(result)
elif operator == "-":
    result = number1 - number2 # subtraction
    print(result)
elif operator == "*":
    result = number1 * number2 # multiplication
    print(result)
else:
    result = number1 / number2 # division
    print(result)

print("thank you for using python calculator!")