number = 6
guess = int(input("enter your guess: "))
is_on = True

while is_on:
    if guess > number:
        print("too high!")
        guess = int(input("enter your guess: "))
    elif guess < number:
        print("too low!")
        guess = int(input("enter your guess: "))
    elif guess == number:
        print("you have guessed right!")
        print(f"the correct number is {number}")
        is_on = False
print("thanks for playing!")