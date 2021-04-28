import random

to_guess = random.randint(0, 99)
user_guess = int(input("Guess a number between 0 and 99: "))
count = 1

not_found = True
while not_found:
    if user_guess < to_guess:
        user_guess = int(input("Too low. Guess again: "))
        count += 1
    elif user_guess < to_guess:
        user_guess = int(input("Too high. Guess again: "))
        count += 1
    else:
        print("Correct. It took you", count, "guesses.")
        not_found = False
