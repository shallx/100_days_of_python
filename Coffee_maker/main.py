from art import logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resource = {
    "water" : 500,
    "milk" : 500,
    "coffee" : 300,
    "money" : 0,
}
    
def checkAvailability(userOption):
    ingredients = MENU[userOption]["ingredients"]
    for key in ingredients:
        if resource[key] < ingredients[key]:
            print(f"Not enough {key}! ")
            return False
    return True

def makeCoffee(userOption):
    ingredients = MENU[userOption]["ingredients"]
    for key in ingredients:
        resource[key] -= ingredients[key]
    resource["money"] += MENU[userOption]["cost"]


def coffeeMaker():
    print(logo)
    while True:
        userMoney = 0
        userOption = input("What would you like? (espresso/latte/cappuccino):").lower()

        while not (userOption == "espresso" or userOption == "latte" or userOption == "cappuccino" or "report"):
            print("Invalid choice, try again!")
            userOption = input("What would you like? (espresso/latte/cappuccino):")

        if userOption == "report":
            print(f"Water: {resource['water']}ml\nMilk: {resource['milk']}ml\nCoffee: {resource['coffee']}g\nMoney: ${resource['money']}")
        else:

            userMoney += int(input("how many quarters?: ")) * .25
            userMoney += int(input("how many dimes?: ")) * .1
            userMoney += int(input("how many nickles?: ")) * .05
            userMoney += int(input("how many pennies?: ")) * .01

            orderCost = MENU[userOption]['cost']
            if orderCost > userMoney:
                print("Sorry that's not enough money. Money refunded.")
            elif checkAvailability(userOption):
                makeCoffee(userOption)
                print(f"Bill: {orderCost} | Changes: {round(userMoney - orderCost, 2)}")
                print(f"Here is your {userOption} ☕️. Enjoy!")

coffeeMaker()
