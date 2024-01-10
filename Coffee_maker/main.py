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

water = 200
milk = 200
coffee = 100
money = 0
resource = {
    "water" : 200,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0,
}

# Make this function work in all regards
def makeCoffee(userOption):
    ingredients = MENU[userOption]["ingredients"]
    if resource["water"] >= ingredients["water"] and resource["coffee"] >= ingredients["coffee"]:
        if "milk" in ingredients and resource["milk"] < ingredients["milk"]:
            print("Sorry! There is not enough milk")
        else: 
            print(f"Here is your {userOption} ☕️. Enjoy!")
    
    

def calcPayment(userOption, quarters, dimes, nickles, pennies):
    return quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01
    # return True if money >= MENU[userOption]["cost"] else False


# TODO: input user
def coffeeMaker():
    
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    userOption = input("What would you like? (espresso/latte/cappuccino):")

    while not (userOption == "espresso" or userOption == "latte" or userOption == "cappuccino"):
        print("Invalid choice, try again!")
        userOption = input("What would you like? (espresso/latte/cappuccino):")
    
    # Printing report
    if userOption == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    
    userMoney = calcPayment(userOption, quarters, dimes, nickles, pennies)

    if MENU[userOption]["cost"] > userMoney:
        print("Sorry that's not enough money. Money refunded.")
    else:
        makeCoffee(userOption, water, milk, coffee, money)


    
    

coffeeMaker()
# TODO: store and help print report
