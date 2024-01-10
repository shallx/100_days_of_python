import os
from art import logo, vs
from game_data import data
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def compare(choiceA, choiceB, ans):
    if ans == "A":
        userGuessed = choiceA
        against = choiceB
    else:
        userGuessed = choiceB
        against = choiceA

    return True if userGuessed["follower_count"] >= against["follower_count"] else False

def printComp(choice, type):
    print(f"Compare {type}: {choice['name']}, a {choice['description']}, from {choice['country']}.")


def play():
    points = 0
    gameEnd = False

    choiceA = random.choice(data)
    print(logo)

    while not gameEnd:
        printComp(choiceA, "A")
        print(vs)
        choiceB = random.choice(data)
        while choiceA == choiceB:
            choiceB = random.choice(data)

        printComp(choiceB, "B")
        ans = input("Who has more followers? Type 'A' or 'B':").upper()

        while ans != "A" and ans != "B":
            print("Invalid choice")
            ans = input("Who has more followers? Type 'A' or 'B:").upper()
        
        isCorrect = compare(choiceA, choiceB, ans)

        cls()
        print(logo)

        if isCorrect:
            points += 1
            print(f"You're right! {choiceA['name']}: {choiceA['follower_count']} | {choiceB['name']}: {choiceB['follower_count']}")
            print(f"Current score: {points}")
            choiceA = choiceB
            choiceB = random.choice(data)
        else:
            print(f"Sorry, that's wrong, {choiceA['name']}: {choiceA['follower_count']} | {choiceB['name']}: {choiceB['follower_count']}")
            print(f"final score: {points}")
            gameEnd = True


play()