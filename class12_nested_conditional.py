# Nested conditionals involve placing one conditional block inside another.
# This is useful for handling complex decision-making scenarios:

age = 12
income = 55000

if age >= 18:
    if income >= 20000:
        print("you qualified for a loan")
    else:
        print("insufficient income")
else:
    print("you need to be 18 to acquired a loan")