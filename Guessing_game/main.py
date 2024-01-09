import random
import art
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard:'").lower()

attemts = 2
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


while not (difficulty == "easy" or difficulty == "hard"):
    print("Invalid selection! Try again")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard:'").lower()

difficulty = EASY_ATTEMPTS if "easy" else HARD_ATTEMPTS # Ternary operator

number = random.randint(1,101)

while attemts > 0:
    print(f"You have {attemts} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low")
    else:
        print(f"You guessed it, the number is {number}")
        attemts = 0

    attemts -= 1

