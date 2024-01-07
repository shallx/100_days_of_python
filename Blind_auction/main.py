import os
from art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

bidFinished = False

winner = {
    "name" : "No one",
    "bid" : 0
}

print(logo)

while not bidFinished:
    name = input("Your name:")
    bid = int(input("Your bid:"))
    bidFinished = input("Are there any other bidders? Type 'yes' or 'no':") == "no"
    if winner["bid"] <= bid:
        winner = {
            "name" : name,
            "bid" : bid,
        }
    if not bidFinished:
        cls()

print(f'The winner is {winner["name"]} with a bid {winner["bid"]}')