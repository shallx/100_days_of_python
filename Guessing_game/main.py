import random
import art
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard:'").lower()

attemts = 10

while not (difficulty == "easy" and not difficulty == "hard"):
    print("Invalid selection! Try again")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard:'").lower()

difficulty = 10 if "easy" else 5 # Ternary operator

number = random.randint(1,101)

while attemts > 0:
    print("You have 10 attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low")
    else:
        print(f"You guessed it, the number is {number}")
        attemts = 0
        
    attemts -= 1

