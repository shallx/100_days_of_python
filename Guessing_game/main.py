import random
import art
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')




EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def get_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard:'").lower()
    if not (difficulty == "easy" or difficulty == "hard"):
        print("Invalid selection! Try again")
        get_difficulty()
    else:
        return difficulty


def play():
    cls()
    won = False
    print(art.logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = get_difficulty()

    attempts = EASY_ATTEMPTS if difficulty == "easy" else HARD_ATTEMPTS # Ternary operator

    number = random.randint(1,101)


    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low")
        else:
            won = True
            attempts = 0

        attempts -= 1

    print((f"You guessed it!" if won == True else "You lost!") + f" The number was {number}")

    shouldRestart = input("Want to start again? y/n:").lower() == "y"
    if shouldRestart:
        play()

play()


